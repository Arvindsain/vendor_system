from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import VendorViewSet, HistorialPerformanceViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"api/vendors", VendorViewSet, basename="vendors")
router.register(r"vendor/historical_performance", HistorialPerformanceViewSet, basename="endor_historical_performance")

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]