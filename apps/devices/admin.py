from django.contrib import admin
from .models import Device, AccessGroupDevices

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'direction', 'device_type')
    search_fields = ('name', 'location')


@admin.register(AccessGroupDevices)
class AccessGroupDevicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    filter_horizontal = ('devices',)  # Для удобного выбора устройств через интерфейс
