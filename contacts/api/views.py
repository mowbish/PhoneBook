from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from contacts.models import (User, Contact, ContactGroup, )
from .serializers import (SignUpSerializer, CreateContactSerializer, ShowAllContactsSerializer,
                          RetrieveContactDetailSerializer, CreateContactGroupSerializer,
                          ShowAllGroupsSerializer, RetrieveContactGroupSerializer)


class SignUpAPIView(CreateAPIView):
    """
        This class for register users to do somethings like
        add Contact or add ContactGroup and other things
    """
    serializer_class = SignUpSerializer
    queryset = User.objects.all()


class CreateContactAPIView(CreateAPIView):
    """
        Each user can create their own contact
    """
    serializer_class = CreateContactSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()


class ShowAllContactsAPIView(ListAPIView):
    """
        User can see their all contacts
    """
    serializer_class = ShowAllContactsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        serializer = ShowAllContactsSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
        Each user can manage their contacts info
        like Remove or Update contact
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveContactDetailSerializer
    lookup_field = "phone_number"

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        serializer = RetrieveContactDetailSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CreateContactGroupAPIView(CreateAPIView):
    """
        With this class APIView clients can create their own
        Group like: close friends, family, colleagues and etc
    """
    serializer_class = CreateContactGroupSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ContactGroup.objects.filter(user=self.request.user)


class ShowAllGroupsAPIView(ListAPIView):
    """
        With this class user can see their all groups
    """
    serializer_class = ShowAllGroupsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ContactGroup.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        serializer = ShowAllGroupsSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class DetailContactGroupAPIView(RetrieveUpdateDestroyAPIView):
    """
        With this class we can manage Group infos like:
        See Groups, Update Groups, Remove Groups and etc
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveContactGroupSerializer
    lookup_field = "name"
