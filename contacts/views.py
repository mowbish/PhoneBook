from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsOwner
from contacts.models import (User, Contact, ContactGroup, )
from contacts.serializers import (SignUpSerializer, CreateContactSerializer,
                                  ContactDetailSerializer, CreateContactGroupSerializer)


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


class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
        Each user can manage their contacts info
        like Remove or Update contact
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ContactDetailSerializer
    lookup_field = "phone_number"

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        serializer = ContactDetailSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CreateContactGroupAPIView(CreateAPIView):
    """
        With this class APIView clients can create their own
        Group like: close friends, family, colleagues and etc
    """
    serializer_class = CreateContactGroupSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        z = ContactGroup.objects.filter(user=self.request.user)
        print(f"\n \n {z}")
        return z

    # def perform_create(self, serializer):
    #     serializer.validated_data['user'] = self.request.user
    #     return super(CreateContactGroupAPIView, self).perform_create(serializer)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class DetailContactGroupAPIView(RetrieveUpdateDestroyAPIView):
    """
        With this class we can manage Group infos like:
        See Groups, Update Groups, Remove Groups and etc
    """
    permission_classes = (IsAuthenticated, IsOwner)
    # serializer_class = ContactGroupSerializer
    lookup_field = "name"

    # def get_queryset(self):
    #     Contact.objects.filter(user=self.request.user)
    #
    # def get(self, request, *args, **kwargs):
    #     serializer = CreateContactSerializer(self.get_queryset(), many=True)
    #     return Response(serializer.data)

# and last of all create extra phone
