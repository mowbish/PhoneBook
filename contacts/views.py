from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from contacts.models import Contact, Phone
from contacts.serializers import ContactSerializer, CreateContactSerializer


class CreateContactAPIView(ListCreateAPIView):
    serializer_class = CreateContactSerializer
    queryset = Contact.objects.all()


class ContactAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
