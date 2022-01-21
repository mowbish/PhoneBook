from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from rest_framework import serializers
from contacts.models import Client, ContactList, ExtraPhone, Contact


class ContactListSerializer(serializers.ModelSerializer):
    # contacts = serializers.StringRelatedField()

    class Meta:
        model = ContactList
        fields = ('name', 'contacts')


class SignUpSerializer(serializers.ModelSerializer):
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = serializers.CharField(validators=[phone_number_regex], max_length=16)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Client
        fields = (
            'phone_number', 'password', 'password2', 'first_name', 'last_name', 'email'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        client = Client.objects.create(
            phone_number=validated_data["phone_number"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],

        )

        client.set_password(validated_data['password'])
        client.save()

        return client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'groups')


class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
