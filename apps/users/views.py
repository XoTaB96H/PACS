from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import User, Role
from django.http import HttpResponse

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/user_list.html', {'users': users})

class UserDetailView(View):
    def get(self, request, pk):
        user_obj = get_object_or_404(User, pk=pk)
        return render(request, 'users/user_detail.html', {'user': user_obj})

class RoleListView(View):
    def get(self, request):
        roles = Role.objects.all()
        return render(request, 'users/role_list.html', {'roles': roles})

class RoleDetailView(View):
    def get(self, request, pk):
        role_obj = get_object_or_404(Role, pk=pk)
        return render(request, 'users/role_detail.html', {'role': role_obj})
