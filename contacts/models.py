from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .managers import CustomUserManager


class Contact(AbstractUser):
    username = None

    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class Phone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
