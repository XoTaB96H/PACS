from django.urls import path
from .views import (DeviceListView, DeviceCreateView, DeviceUpdateView, DeviceDeleteView,
                    AccessGroupDevicesListView, AccessGroupDevicesCreateView, AccessGroupDevicesUpdateView,
                    AccessGroupDevicesDeleteView)

app_name = 'devices'

urlpatterns = [
    # Устройства
    path('', DeviceListView.as_view(), name='device_list'),
    path('create/', DeviceCreateView.as_view(), name='device_create'),
    path('<int:pk>/edit/', DeviceUpdateView.as_view(), name='device_edit'),
    path('<int:pk>/delete/', DeviceDeleteView.as_view(), name='device_delete'),

    # Группы устройств
    path('groups/', AccessGroupDevicesListView.as_view(), name='group_list'),
    path('groups/create/', AccessGroupDevicesCreateView.as_view(), name='group_create'),
    path('groups/<int:pk>/edit/', AccessGroupDevicesUpdateView.as_view(), name='group_edit'),
    path('groups/<int:pk>/delete/', AccessGroupDevicesDeleteView.as_view(), name='group_delete'),
]
