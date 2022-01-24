from django.urls import path, include

urlpatterns = [
    # Path and rout for version1 API
    path('v1/', include('contacts.api.urls')),
]
