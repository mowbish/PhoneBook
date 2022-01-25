from django.urls import path

from .views import (SignUpAPIView, CreateContactAPIView, ShowAllContactsAPIView,
                    ContactDetailAPIView, CreateContactGroupAPIView, ShowAllGroupsAPIView,
                    DetailContactGroupAPIView)

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('create/contact/', CreateContactAPIView.as_view(), name='create-contact'),
    path('contacts/', ShowAllContactsAPIView.as_view(), name='contacts'),
    path('contact/<str:phone_number>/', ContactDetailAPIView.as_view(), name='detail-contact'),
    path('create/group/', CreateContactGroupAPIView.as_view(), name='create-group'),
    path('groups/', ShowAllGroupsAPIView.as_view(), name='groups'),
    path('group/<str:name>/', DetailContactGroupAPIView.as_view(), name='detail-group'),
]
