from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django import forms
from django.urls import reverse
from .models import Credential
from apps.users.models import User

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['user', 'credential_type', 'credential_value', 'is_active']

class CredentialListView(View):
    def get(self, request):
        credentials = Credential.objects.select_related('user').all()
        return render(request, 'credentials/credential_list.html', {'credentials': credentials})

class CredentialCreateView(View):
    def get(self, request):
        form = CredentialForm()
        return render(request, 'credentials/credential_form.html', {'form': form})

    def post(self, request):
        form = CredentialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('credentials:credential_list'))
        return render(request, 'credentials/credential_form.html', {'form': form})

class CredentialUpdateView(View):
    def get(self, request, pk):
        cred = get_object_or_404(Credential, pk=pk)
        form = CredentialForm(instance=cred)
        return render(request, 'credentials/credential_form.html', {'form': form, 'credential': cred})

    def post(self, request, pk):
        cred = get_object_or_404(Credential, pk=pk)
        form = CredentialForm(request.POST, instance=cred)
        if form.is_valid():
            form.save()
            return redirect(reverse('credentials:credential_list'))
        return render(request, 'credentials/credential_form.html', {'form': form, 'credential': cred})

class CredentialDeleteView(View):
    def get(self, request, pk):
        cred = get_object_or_404(Credential, pk=pk)
        return render(request, 'credentials/credential_confirm_delete.html', {'credential': cred})

    def post(self, request, pk):
        cred = get_object_or_404(Credential, pk=pk)
        cred.delete()
        return redirect(reverse('credentials:credential_list'))
