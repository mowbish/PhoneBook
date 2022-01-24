from django.test import TestCase

from contacts.models import User


class SignUpTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="lion", sound="roar")
        User.objects.create(name="cat", sound="meow")

    def test_can_register(self):
        """Animals that can speak are correctly identified"""
        data = {
            'Phone_number' : "s"
        }
        self.client.post('signup', data=data)
        # cat = Animal.objects.get(name="cat")
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')
