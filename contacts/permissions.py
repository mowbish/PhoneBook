from rest_framework import permissions
from .models import User, Contact


class IsOwner(permissions.BasePermission):
    """
       Object-level permission to only allow updating his own profile
    """

    def has_permission(self, request, view):
        return request.user == Contact.objects.get(phone_number=view.kwargs['phone_number'])

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # obj here is a UserProfile instance
        return obj.user == request.user
