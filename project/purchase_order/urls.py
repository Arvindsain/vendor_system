from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import PurchaseOrderViewSet

router = DefaultRouter()
router.register(r"api/purchase_orders", PurchaseOrderViewSet, basename="purchase-orders")

urlpatterns = [
    path('', include(router.urls)),
]