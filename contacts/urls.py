from django.urls import path, include

from contacts.views import ContactAPIView, CreateContactAPIView

urlpatterns = [
    path('<int:pk>', ContactAPIView.as_view(), name='contacts'),
    path('create/', CreateContactAPIView.as_view(), name='create'),
]
