from django.contrib import admin
from .models import Credential

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'credential_type', 'credential_value', 'is_active')
    search_fields = ('credential_value', 'user__first_name', 'user__last_name')
    list_filter = ('credential_type', 'is_active')
