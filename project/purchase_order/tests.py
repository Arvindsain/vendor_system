from django.test import TestCase
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class PurchaseOrderModelTestCase(TestCase):
    def setUp(self):
        # Setting up the test client and superuser
        self.vendor_id = None
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(username="testsuperuser", password="testpassword")
        resp = self.client.post(
            "/api/token/",
            dict(username="testsuperuser", password="testpassword"),
            format="json"
        )
        assert resp.status_code == 200
        self.token = resp.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_vendor_create(self):
        # create vendor for purchase order
        data = dict(
            name="Vendor1",
            contact_details="Contact info 1",
            address="Test Address 1",
            on_time_delivery_rate=95.0,
            quality_rating_avg=4.5,
            average_response_time=24.5,
            fulfillment_rate=90.0
        )
        resp = self.client.post(
            "/api/vendors/",
            data=data,
            format="json"
        )
        assert resp.status_code == 201
        assert resp.data["name"] == "Vendor1"
        assert resp.data["vendor_code"] is not None
        self.vendor_id = resp.data["id"]

    def test_purchase_order_creation(self):
        # Test for PurchaseOrder creation
        self.test_vendor_create()
        data = dict(
            vendor=self.vendor_id,
            order_date=datetime.now(),
            delivery_date=datetime.now() + timedelta(days=7),
            items={'item1': 'description1', 'item2': 'description2'},
            quantity=10,
            issue_date=datetime.now(),
        )
        resp = self.client.post(
            "/api/purchase_orders/",
            data=data,
            format="json"
        )
        breakpoint()
        assert resp.status_code == 201
        assert resp.data["po_number"] is not None # po_number is auto created.
        self.purchase_id = resp.data["id"]

    def test_get_purchase_order(self):
        # get specific purchase order with id
        self.test_purchase_order_creation()
        url = f"/api/purchase_orders/{self.purchase_id}/"

        resp = self.client.get(url)
        assert resp.status_code == 200
        assert resp.data["id"] == self.vendor_id
    
    def test_acknowledgement(self):
        # Test acknowledgement endpoint
        self.test_purchase_order_creation()
        url = f"/api/purchase_orders/{self.purchase_id}/acknowledge/"
        resp = self.client.post(
            url,
        )
        assert resp.status_code == 200
        assert resp.data["message"] == "Acknowledged successfully"


        
