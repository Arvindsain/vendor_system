from rest_framework import serializers
from .models import Vendor, HistoricalPerformance

class VendorSz(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            "id",
            "name",
            "contact_details",
            "address",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate"
        )
        read_only = (
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
            "vendor_code",
        )

class HistoricalPerformanceSz(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"