from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Q
from .models import AccessLog
from django import forms

class LogFilterForm(forms.Form):
    credential_value = forms.CharField(required=False, label='Credential Value')
    device_name = forms.CharField(required=False, label='Device Name')
    result = forms.ChoiceField(choices=[('', '---'), ('granted', 'Разрешено'), ('denied', 'Запрещено')], required=False, label='Результат')

class AccessLogListView(View):
    def get(self, request):
        form = LogFilterForm(request.GET or None)
        logs = AccessLog.objects.select_related('credential', 'device', 'credential__user').all()

        if form.is_valid():
            credential_value = form.cleaned_data.get('credential_value')
            device_name = form.cleaned_data.get('device_name')
            result = form.cleaned_data.get('result')

            if credential_value:
                logs = logs.filter(credential__credential_value__icontains=credential_value)
            if device_name:
                logs = logs.filter(device__name__icontains=device_name)
            if result:
                logs = logs.filter(result=result)

        logs = logs.order_by('-timestamp')

        return render(request, 'access_logs/log_list.html', {'logs': logs, 'form': form})

class AccessLogDetailView(View):
    def get(self, request, pk):
        log_entry = get_object_or_404(AccessLog, pk=pk)
        return render(request, 'access_logs/log_detail.html', {'log': log_entry})
