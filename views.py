from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from.forms import OrderForm, CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
    		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)    
    
    
"""
    form = CreateUserForm()

    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'student/register.html', context)
"""


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    #else:
        #create user with sql
    context={}
    return render(request, 'student/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')




def home(request):
    return render(request, 'student/dashboard.html')

def progress(request):
    return render(request,'student/progress.html')

def statistics(request):
    return render(request,'student/statistics.html')


