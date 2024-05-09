from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class VendorEndpointTestCase(TestCase):
    def setUp(self):
        self.vendor_id = None
        # Setting up the test client and superuser
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
        # vendor creation endpoint test
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

        # vendor2 
        data = dict(
            name="Vendor2",
            contact_details="Contact info 2",
            address="Test Address 2",
            on_time_delivery_rate=85.0,
            quality_rating_avg=4.7,
            average_response_time=20.5,
            fulfillment_rate=70.0
        )
        resp = self.client.post(
            "/api/vendors/",
            data=data,
            format="json"
        )
        assert resp.status_code == 201

    def test_get_vendor(self):
        # get specific vendor details
        self.test_vendor_create()
        
        url = f"/api/vendors/{self.vendor_id}/"

        resp = self.client.get(url)
        assert resp.status_code == 200
        assert resp.data["id"] == self.vendor_id

    def test_get_all_vendors(self):
        # get all vendors
        self.test_vendor_create()
        url = "/api/vendors/"
        resp = self.client.get(url)
        assert resp.status_code == 200
        assert len(resp.data["results"]) == 2