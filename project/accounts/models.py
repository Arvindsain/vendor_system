import uuid
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            # Generate a unique vendor code
            self.vendor_code = f"V-{str(uuid.uuid4()).replace('-', '')[:5].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('accounts.Vendor', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"