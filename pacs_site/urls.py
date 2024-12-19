from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def index(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('users/', include('apps.users.urls', namespace='users')),
    path('devices/', include('apps.devices.urls', namespace='devices')),
    path('credentials/', include('apps.credentials.urls', namespace='credentials')),
    path('logs/', include('apps.access_logs.urls', namespace='access_logs')),
    path('api/', include('apps.api.urls', namespace='api')),
]
