from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from rest_framework import serializers
from contacts.models import Contact, Phone


class CreateContactSerializer(serializers.ModelSerializer):
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = serializers.CharField(validators=[phone_number_regex], max_length=16)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Contact
        fields = (
            'phone_number', 'password', 'password2'
        )


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        contact = Contact.objects.create(
            phone_number=validated_data["phone_number"],


        )

        contact.set_password(validated_data['password'])
        contact.save()

        return contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
