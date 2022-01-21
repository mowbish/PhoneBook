from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Contact(User):

    def __str__(self):
        return self.username


class Phone(models.Model):
    contact = models.ForeignKey(Contact)
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
