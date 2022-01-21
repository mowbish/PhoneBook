from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .managers import CustomUserManager


class Client(AbstractUser):
    username = None

    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class Contact(models.Model):
    creator = models.ForeignKey(Client, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)
    email = models.EmailField(unique=True, blank=True)
    birth_day = models.DateField(blank=True)
    description = models.TextField(max_length=550)

    def __str__(self):
        return self.first_name + " " + self.last_name


class ContactList(models.Model):
    name = models.CharField(max_length=150)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name


class ExtraPhone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)
