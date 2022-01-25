from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from conf.utils import phone_number_regex
from contacts.models import User, ContactGroup, ExtraPhone, Contact
from django.contrib.auth.password_validation import validate_password


class SignUpSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[phone_number_regex], max_length=16)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'phone_number', 'password', 'confirm_password', 'first_name', 'last_name', 'email'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        client = User.objects.create(
            phone_number=validated_data["phone_number"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],

        )

        client.set_password(validated_data['password'])
        client.save()

        return client


class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('user',)

    def create(self, validated_data):
        contact = Contact.objects.create(
            user=self.context['request'].user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            birth_day=validated_data['birth_day'],
            description=validated_data['description'],
        )
        contact.save()
        return contact


class ShowAllContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class RetrieveContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(user=request.user)


class CreateContactGroupSerializer(serializers.ModelSerializer):
    contacts = UserFilteredPrimaryKeyRelatedField(queryset=Contact.objects, many=True, write_only=True)

    class Meta:
        model = ContactGroup
        exclude = ('user',)

    def create(self, validated_data):
        contact_group = ContactGroup.objects.create(
            name=validated_data['name'],
            user=self.context['request'].user,
        )

        contact_group.contacts.set(validated_data['contacts'])
        contact_group.save()
        return contact_group

    def validate(self, attrs):
        contacts = attrs['contacts']
        for contact in contacts:
            if contact.user != self.context['request'].user:
                raise ValidationError("you dont have permission to this user")
        return attrs


class ShowAllGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactGroup
        fields = "__all__"


class RetrieveContactGroupSerializer(serializers.ModelSerializer):
    contacts = CreateContactSerializer(many=True)
    user = UserSerializer(many=False)

    class Meta:
        model = ContactGroup
        fields = "__all__"
