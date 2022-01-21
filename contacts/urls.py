from django.urls import path

from contacts.views import ClientAPIView, SignUpAPIView, CreateContactAPIView,CreateContactListAPIView

urlpatterns = [

    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('create/contact', CreateContactAPIView.as_view(), name='create-contact-list'),
    path('create/contact-list', CreateContactListAPIView.as_view(), name='create-contact-list'),
    path('<str:name>', ClientAPIView.as_view(), name='contact'),
]
