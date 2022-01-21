from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from contacts.models import Contact, Phone
from contacts.serializers import ContactSerializer, CreateContactSerializer


class ShowAllContactsAPIView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class CreateContactAPIView(ListCreateAPIView):
    serializer_class = CreateContactSerializer
    queryset = Contact.objects.all()


class ContactAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = "phone_number"
