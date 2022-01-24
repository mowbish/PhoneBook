from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Group
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from .managers import CustomUserManager

from PhoneBook.utils import phone_number_regex


class User(AbstractUser):
    username = None
    CLIENT = 'CLIENT'

    # If it was mentioned in the task that we need
    # an admin, a field called admin would be created,
    # but since it is not said, then we do not write anything.
    user_type_choices = (
        (CLIENT, 'CLIENT'),
    )
    user_type = models.CharField(choices=user_type_choices, default=CLIENT)
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    phone_number = models.CharField(
        validators=[phone_number_regex],
        max_length=16,
        unique=True)
    email = models.EmailField(blank=True)
    birth_day = models.DateField(blank=True)
    description = models.TextField(max_length=550)

    def __str__(self):
        return self.first_name + " " + self.last_name


class ContactGroup(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name

    def clean(self):
        for contact in self.contacts.all():
            if contact.user != self.user:
                raise ValidationError("this contact that you have been selected is not created by you")


class ExtraPhone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)

    def __str__(self):
        return self.phone_number
