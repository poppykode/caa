from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import (
    UserCreateForm ,
) 
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#FBV
def LoginView(request):
    return render(request,'_admin/login.html')
@login_required
def DashboardView(request):
    return render(request,'_admin/dashboard.html')

@login_required
def RegisterView(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been successfully created!')
            return redirect(reverse('_admin:register'))
    else:
        form = UserCreateForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def StuffMembersListView(request):
    staff = User.objects.all()
    return render(request,'_admin/stafflist.html',{'staff':staff})
    
@login_required
def EditUserView(request,user):
    user = request.user.id
    print(user)
    user.is_active = False
    messages.success(request, 'Profile successfully disabled.')
    return redirect(reverse('_admin:stuff-members'))

@login_required
def disable_user_view(request,user):
    user = request.user
    print(type(user))
    user.is_active = False
    messages.success(request, 'Profile successfully disabled.')
    return redirect(reverse('_admin:stuff-members'))
#CBV
class StuffMembersListView(LoginRequiredMixin,ListView):
    template_name = '_admin/stafflist.html'
    context_object_name = 'staff_list'
    model = User
