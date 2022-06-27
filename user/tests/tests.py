import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestUser(TestCase):

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

    def test_sign_up_user(self):
        """Test sign up user successfully."""
        response = self.client.post(
            reverse("user:create"), data=json.dumps(
                self.sign_up_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_sign_up_user_with_no_password(self):
        """Test sign up user with no password."""
        self.sign_up_data['password'] = ''
        response = self.client.post(
            reverse("user:create"), data=json.dumps(
                self.sign_up_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_user_successfully(self):
        """Test login user successfully."""
        # First sign up.
        self.client.post(
            reverse("user:create"), data=json.dumps(
                self.sign_up_data), content_type='application/json')
        # Then, login.
        response = self.client.post(
            reverse("user:login"), data=json.dumps(
                self.login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_with_no_email(self):
        """Test login with no email."""

        # First sign up.
        self.client.post(
            reverse("user:create"), data=json.dumps(
                self.sign_up_data), content_type='application/json')
        # Then, login.
        self.login_data['email'] = ''
        response = self.client.post(
            reverse("user:login"), data=json.dumps(
                self.login_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
