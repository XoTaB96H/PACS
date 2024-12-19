from django.urls import path
from .views import (
    CredentialListView,
    CredentialCreateView,
    CredentialUpdateView,
    CredentialDeleteView
)

app_name = 'credentials'

urlpatterns = [
    path('', CredentialListView.as_view(), name='credential_list'),
    path('create/', CredentialCreateView.as_view(), name='credential_create'),
    path('<int:pk>/edit/', CredentialUpdateView.as_view(), name='credential_edit'),
    path('<int:pk>/delete/', CredentialDeleteView.as_view(), name='credential_delete'),
]
