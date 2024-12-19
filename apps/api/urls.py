from django.urls import path
from .views import CheckAccessView

app_name = 'api'

urlpatterns = [
    path('check_access/', CheckAccessView.as_view(), name='check_access'),
]
