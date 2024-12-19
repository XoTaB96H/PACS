from django import forms
from .models import User, Role

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'photo', 'is_active', 'roles']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'username', 'password_hash', 'description', 'access_group_devices']
