from django.urls import path

from .views import (SignUpAPIView, CreateContactAPIView,
                            ContactDetailAPIView, CreateContactGroupAPIView, DetailContactGroupAPIView)

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('create/contact/', CreateContactAPIView.as_view(), name='create-contact'),
    path('contact/<str:phone_number>/', ContactDetailAPIView.as_view(), name='detail-contact'),
    path('create/group/', CreateContactGroupAPIView.as_view(), name='create-group'),
    path('group/<str:name>/', ContactDetailAPIView.as_view(), name='detail-group'),
]
