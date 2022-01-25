from django.urls import reverse
from rest_framework import status
from .models import User, Contact
from rest_framework.test import APITestCase, APIClient


class SignUpTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            phone_number='9999255351',
            first_name='Mobin',
            last_name='Aghaei',
            email='mobin.agaei@gmail.com',
        )

        self.user2 = User.objects.create_user(
            phone_number='9911223344',
            first_name='Hassan',
            last_name='khoshtinat',
            email='Hassan.khoshtinat@gmail.com',
        )

    def test_sign_up_user(self):
        url = reverse('signup')

        valid_data = {
            "phone_number": '9988773344',
            "first_name": 'Ali',
            "last_name": 'Hassani',
            "email": 'Ali.Hassani@gmail.com',
            "password": "MohsenMohsen1333",
            "confirm_password": "MohsenMohsen1333"
        }

        invalid_data = {
            "phone_number": '',
            "first_name": 'Reza',
            "last_name": 'Mohseni',
            "email": 'Reza.Mohseni@gmail.com',
            "password": "MohsenMohsen1333",
            "confirm_password": "MohsenMohsen1333"
        }

        response = self.client.post(path=url, data=valid_data)
        response2 = self.client.post(path=url, data=invalid_data)

        self.assertEquals(User.objects.count(), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)


class AccountTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            phone_number='9999255351',
            first_name='Mobin',
            last_name='Aghaei',
            email='mobin.agaei@gmail.com',
            password="MohsenMohsen1333",

        )

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """

        # user = User.objects.create_user('username', 'Pas$w0rd')
        # self.assertTrue(self.client.login(username='username', password='Pas$w0rd'))
        # response = self.client.get(reverse('create-contact'))
        # self.assertEqual(response.status_code, httplib.OK)

        # user = User.objects.get(phone_number=self.user1.phone_number)
        # client = APIClient()
        # print('iammmmmm moniiiiiiinnnnnn')
        # print(client.login(phone_number=self.user1.phone_number, password=self.user1.password))

        login_url = "/api-auth/login/"
        login_data = {
            # "user": "1",
            # "first_name": "contact_one_first_name",
            # "last_name": "contact_one_last_name",
            "phone_number": "9999255351",
            "password": "MohsenMohsen1333",
            # "email": "contact_one@gmail.com",
            # "birth_day": "01/26/2022",

        }
        create_contact_url = reverse('create-contact')
        contact_data = {
            "user": "1",
            "first_name": "contact_one_first_name",
            "last_name": "contact_one_last_name",
            "phone_number": "9999255351",
            "email": "contact_one@gmail.com",
            "birth_day": "01/26/2022",
        }

        response1 = self.client.post(path=login_url, data=login_data)
        response2 = self.client.post(path=create_contact_url, data=contact_data)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)


