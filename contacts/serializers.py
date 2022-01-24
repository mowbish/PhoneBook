from rest_framework import serializers
from conf.utils import phone_number_regex
from contacts.models import User, ContactGroup, ExtraPhone, Contact
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Group


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
    creator_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        contact = Contact.objects.create(
            user=validated_data['user'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            birth_day=validated_data['birth_day'],
            description=validated_data['description'],
        )
        contact.save()
        return contact


class ContactDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CreateContactGroupSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # print(f"\n{serializers.CurrentUserDefault()}\n")
    # print(f"\n{user.}\n")
    # user = serializers.ReadOnlyField(source='User.username')

    user = serializers.SerializerMethodField()

    class Meta:
        model = ContactGroup
        fields = '__all__'

    def create(self, validated_data):
        contact_group = ContactGroup.objects.create(
            name=validated_data['name'],
            user=validated_data['user'],
        )

        contact_group.contacts.set(validated_data['contacts'])
        contact_group.save()
        return contact_group

    def get_user(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        return user
