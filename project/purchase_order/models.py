from django.db import models

class PurchaseOrder(models.Model):

    class Status(models.TextChoices):
        pending = ("pending", "Pending")
        completed = ("completed", "Completed")
        canceled = ("canceled", "Canceled")

    po_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    vendor = models.ForeignKey('accounts.Vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=Status.choices,default=Status.pending)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    #Generate Po number
    def generate_po_number(self):
        #get last po_number
        last_po = PurchaseOrder.objects.order_by('id').last()
        if last_po:
            last_id = last_po.id
            new_id = last_id + 1
        else:
            new_id = 1
        return f"PO{new_id:010d}"

    def save(self, *args, **kwargs):    
        if not self.po_number:
            self.po_number = self.generate_po_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.po_number