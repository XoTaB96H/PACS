from django.contrib import admin
from .models import User, Role, UserRole, AccessGroupDevices

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'is_active')
    search_fields = ('first_name', 'last_name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'access_group_devices')
    search_fields = ('name', 'username')

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')

@admin.register(AccessGroupDevices)
class AccessGroupDevicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
