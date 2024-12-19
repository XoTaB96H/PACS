from django.contrib import admin
from .models import Device, AccessGroupDevices, AccessGroupDevicesMap

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'direction', 'device_type')
    search_fields = ('name', 'location')

@admin.register(AccessGroupDevices)
class AccessGroupDevicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(AccessGroupDevicesMap)
class AccessGroupDevicesMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'access_group_devices', 'device')
    list_filter = ('access_group_devices',)
