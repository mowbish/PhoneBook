from django.test import TestCase
from django.urls import reverse
from .models import User
import json
from django.test import Client
from rest_framework import status
client = Client()


class SignUpTestCase(TestCase):
    def setUp(self):
        self.valid_payload = {
            "phone_number": "9999255351",
            "first_name": "Mobin",
            "last_name": "Aghaei",
            "email": "mobin.agaei@gmail.com",
        }
        self.invalid_payload = {
            "phone_number": "mzdf",
            "first_name": "",
            "last_name": "",
            "email": "",
        }
    def test_valid_sign_up(self):
        response = client.post(
            reverse('signup'),
            data = json.dumps(self.valid_payload),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_invalid_sign_up(self):
        response = client.post(
            reverse('signup'),
            data = json.dumps(self.invalid_payload),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetContactDetailTest(TestCase):
    def setUp(self):
        self.mobin = User.objects.create(
                    phone_number='9999255351',
                    first_name='Mobin',
                    last_name='Aghaei',
                    email='mobin.agaei@gmail.com',
                )

    def test_get_valid_contact_detail(self):
        pass
