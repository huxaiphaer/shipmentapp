import json
from unittest import TestCase
from rest_framework.test import APIClient

from django.urls import reverse


class TestShipment(TestCase):

    def setUp(self):
        self.sign_up_data = {"username": "huxy",
                             "email": "huxy@gmail.com",
                             "password": "namungoona"
                             }
        self.login_data = {
            "email": "huxy@gmail.com",
            "password": "namungoona"
        }
        self.client = APIClient()

        self.shipment_data = {
            "package_name": "Bread",
            "shipping_date": "2022-06-12",
            "arrival_date": "2022-07-05",
            "status": "PD",
            "country_of_origin": "UG",
            "destination_country": "UG"
        }

        token = self.login_template().data.get(
            "tokens", None).get("access", None)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {0}".format(token))

    def login_template(self):
        """Login template for tests"""
        self.client.post(
            reverse("user:create"), data=json.dumps(
                self.sign_up_data), content_type='application/json')
        # Then, login.
        response = self.client.post(
            reverse("user:login"), data=json.dumps(
                self.login_data), content_type='application/json')
        return response

    def test_add_shipments_successfully(self):
        """Add shipments successfully."""
        response = self.client.post(
            reverse("shipment"), data=json.dumps(
                self.shipment_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_shipment_missing_data(self):
        """Test add shipments missing data."""
        del self.shipment_data['arrival_date']
        del self.shipment_data['country_of_origin']
        response = self.client.post(
            reverse("shipment"), data=json.dumps(
                self.shipment_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_all_shipments(self):
        """Test get all shipments."""
        response = self.client.get(
            reverse("shipment"), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_shipment(self):
        """Test get one shipment."""
        shipment = self.client.post(
            reverse("shipment"), data=json.dumps(
                self.shipment_data), content_type='application/json')

        url = '/api/v1/shipments/{}/'.format(shipment.data.get('uuid'))

        response = self.client.get(
            url,
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def tests_edit_single_shipment(self):
        """Edit single shipment."""
        shipment = self.client.post(
            reverse("shipment"), data=json.dumps(
                self.shipment_data), content_type='application/json')

        url = '/api/v1/shipments/{}/'.format(shipment.data.get('uuid'))

        self.shipment_data['package_name'] = 'Maize'

        response = self.client.patch(
            url, data=json.dumps(
                self.shipment_data),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def tests_delete_single_shipment(self):
        """Delete single shipment."""
        shipment = self.client.post(
            reverse("shipment"), data=json.dumps(
                self.shipment_data), content_type='application/json')

        url = '/api/v1/shipments/{}/'.format(shipment.data.get('uuid'))

        self.shipment_data['package_name'] = 'Maize'

        response = self.client.delete(
            url, content_type='application/json')
        self.assertEqual(response.status_code, 200)


