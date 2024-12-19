from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Device, AccessGroupDevices
from django.urls import reverse
from django import forms

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'location', 'direction', 'device_type']

class AccessGroupDevicesForm(forms.ModelForm):
    class Meta:
        model = AccessGroupDevices
        fields = ['name']


# Список устройств
class DeviceListView(View):
    def get(self, request):
        devices = Device.objects.all()
        return render(request, 'devices/device_list.html', {'devices': devices})


# Добавление устройства
class DeviceCreateView(View):
    def get(self, request):
        form = DeviceForm()
        return render(request, 'devices/device_form.html', {'form': form})

    def post(self, request):
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('devices:device_list'))
        return render(request, 'devices/device_form.html', {'form': form})


# Редактирование устройства
class DeviceUpdateView(View):
    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        form = DeviceForm(instance=device)
        return render(request, 'devices/device_form.html', {'form': form, 'device': device})

    def post(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect(reverse('devices:device_list'))
        return render(request, 'devices/device_form.html', {'form': form, 'device': device})


# Удаление устройства
class DeviceDeleteView(View):
    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        return render(request, 'devices/device_confirm_delete.html', {'device': device})

    def post(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        device.delete()
        return redirect(reverse('devices:device_list'))


# Аналогично для групп устройств
class AccessGroupDevicesListView(View):
    def get(self, request):
        groups = AccessGroupDevices.objects.all()
        return render(request, 'devices/access_group_list.html', {'groups': groups})


class AccessGroupDevicesCreateView(View):
    def get(self, request):
        form = AccessGroupDevicesForm()
        return render(request, 'devices/access_group_form.html', {'form': form})

    def post(self, request):
        form = AccessGroupDevicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('devices:group_list'))
        return render(request, 'devices/access_group_form.html', {'form': form})


class AccessGroupDevicesUpdateView(View):
    def get(self, request, pk):
        group = get_object_or_404(AccessGroupDevices, pk=pk)
        form = AccessGroupDevicesForm(instance=group)
        return render(request, 'devices/access_group_form.html', {'form': form, 'group': group})

    def post(self, request, pk):
        group = get_object_or_404(AccessGroupDevices, pk=pk)
        form = AccessGroupDevicesForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect(reverse('devices:group_list'))
        return render(request, 'devices/access_group_form.html', {'form': form, 'group': group})


class AccessGroupDevicesDeleteView(View):
    def get(self, request, pk):
        group = get_object_or_404(AccessGroupDevices, pk=pk)
        return render(request, 'devices/access_group_confirm_delete.html', {'group': group})

    def post(self, request, pk):
        group = get_object_or_404(AccessGroupDevices, pk=pk)
        group.delete()
        return redirect(reverse('devices:group_list'))
