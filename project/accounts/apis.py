import django_filters
from .permissions import IsSuperuser
from .models import Vendor, HistoricalPerformance
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import VendorSz, HistoricalPerformanceSz
from rest_framework import viewsets, response, decorators

class VendorFilter(django_filters.FilterSet):
    class Meta:
        model = Vendor
        fields = {
            "name": ("exact", "icontains", "contains"),
            "vendor_code": ("exact",)
        }

class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSz
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    filterset_class = VendorFilter

    def get_queryset(self):
        return Vendor.objects.all().order_by("-id")
    
    @decorators.action(detail=True, methods=['GET'], url_path='performance')
    def vendor_performance(self, request, pk):
        """
        api used return performance matrix of vendor.

        Args:
        - request: GET
        - request: HTTP request object.
        - pk (int): Primary key of the vendor instance.

        Returns:
        - Response: return the performance matrix of vendor.
        """
        try:
            vendor = Vendor.objects.get(id=pk)
            performance_metrics = {
                'vendor_name': vendor.name,
                'on_time_delivery_rate':vendor.on_time_delivery_rate,
                'quality_rating_avg':vendor.quality_rating_avg,
                'average_response_time':vendor.average_response_time,
                'fulfillment_rate':vendor.fulfillment_rate
            }
            return response.Response(performance_metrics)
        except Vendor.DoesNotExist:
            return response.Response({"error": "Vendor not found in system."})

class HistorialPerformanceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HistoricalPerformanceSz
    permission_classes = [IsSuperuser]

    def get_queryset(self):
        vendor_id = self.request.query_params.get('vendor_id')
        breakpoint()
        if vendor_id is not None:
            queryset = HistoricalPerformance.objects.filter(vendor=vendor_id).order_by("-date")
        else:
            queryset = HistoricalPerformance.objects.all().order_by("-date")
            
        return queryset