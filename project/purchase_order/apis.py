import django_filters
from django.utils import timezone
from .models import PurchaseOrder
from .serializers import PurchaseOrderSz
from accounts.permissions import IsSuperuser
from rest_framework import viewsets, decorators, response

class PurchaseOrderFilter(django_filters.FilterSet):
    class Meta:
        model = PurchaseOrder
        fields = {
            "vendor_id": ("exact",),
            "order_date": ("exact", "lt", "gt", "lte", "gte"),
            "status": ("exact",)
        }

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderSz
    permission_classes = [IsSuperuser]
    filterset_class = PurchaseOrderFilter

    def get_queryset(self):
        return PurchaseOrder.objects.all().order_by("-order_date")
    
    @decorators.action(detail=True, methods=["POST"], url_path="acknowledge")
    def acknowledge(self, request, pk):
        try:
            perchase_order = PurchaseOrder.objects.get(id=pk)
            if not perchase_order.acknowledgment_date:
                perchase_order.acknowledgment_date = timezone.now()
                perchase_order.save()
                return response.Response({'status': 'Acknowledged successfully'})

        except PurchaseOrder.DoesNotExist:
            return response.Response({"error": "PurchaseOrder not found in system."})
