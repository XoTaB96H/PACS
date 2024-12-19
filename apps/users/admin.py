from django.contrib import admin
from .models import User, Role

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'is_active', 'role')
    search_fields = ('first_name', 'last_name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'access_group_devices')
    search_fields = ('name', 'username')
