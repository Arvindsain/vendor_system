from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSz(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = (
            "id",
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgment_date",
        )
        read_only = (
            "po_number",
            "acknowledgment_date",
        )
    
    # Validates the quantity field
    def validate_quantity(self,value):
        if value <= 0:
            raise serializers.ValidationError('Quantity Cannot be less than 1')
        return value

    # Validates the quality_rating field
    def validate_quality_rating(self,value):
        current_status = self.instance.status
        if current_status.lower() != 'completed':
            raise serializers.ValidationError('Cannot give Quality rating ')
        if value not in range(1,11):
            raise serializers.ValidationError('Quality Rating must between 1-10')
        
        return value