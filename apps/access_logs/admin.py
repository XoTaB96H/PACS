from django.contrib import admin
from .models import AccessLog

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'credential', 'device', 'direction', 'result')
    search_fields = ('credential__credential_value', 'device__name')
    list_filter = ('direction', 'result', 'timestamp')
