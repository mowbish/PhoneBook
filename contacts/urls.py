from django.urls import path

from contacts.views import ContactAPIView, CreateContactAPIView, ShowAllContactsAPIView

urlpatterns = [
    path('', ShowAllContactsAPIView.as_view(), name='contacts'),
    path('<int:phone_number>', ContactAPIView.as_view(), name='contact'),
    path('create/', CreateContactAPIView.as_view(), name='create'),
]
