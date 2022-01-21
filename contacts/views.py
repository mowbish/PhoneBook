from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from contacts.models import Client, ExtraPhone, ContactList, Contact
from contacts.serializers import ClientSerializer, SignUpSerializer, ContactListSerializer, CreateContactSerializer


class SignUpAPIView(ListCreateAPIView):
    serializer_class = SignUpSerializer
    queryset = Client.objects.all()


class CreateContactListAPIView(ListCreateAPIView):
    serializer_class = ContactListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ContactList.objects.all()


class ClientAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactListSerializer
    queryset = ContactList.objects.all()
    lookup_field = "name"


class CreateContactAPIView(ListCreateAPIView):
    serializer_class = CreateContactSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()

    def post(self, request, *args, **kwargs):
        pass
