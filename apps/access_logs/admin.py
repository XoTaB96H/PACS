from django.contrib import admin
from .models import AccessLog

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'credential', 'device', 'direction', 'result')
    search_fields = ('credential__credential_value', 'device__name', 'result')
    list_filter = ('direction', 'result', 'timestamp')
    readonly_fields = ('credential', 'device', 'timestamp', 'direction', 'result', 'additional_info')

    def has_add_permission(self, request):
        return False  # Запрещает добавление новых записей

    def has_change_permission(self, request, obj=None):
        return False  # Запрещает изменение записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещает удаление записей
