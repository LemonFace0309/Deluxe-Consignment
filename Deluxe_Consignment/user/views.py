from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST.copy())

        if form.is_valid():
            user, created = User.objects.get_or_create(username=form.cleaned_data['email'],
                                                       email=form.cleaned_data['email'],
                                                       first_name=form.cleaned_data['first_name'],
                                                       last_name=form.cleaned_data['last_name'])

            if created:
                user.set_password(form.cleaned_data['password2'])
                user.save()
                messages.success(request, 'Account created successfully')
            else:
                messages.success(request, 'Account already exists')
        else:
            messages.error(request, 'ERROR SAVING FORM: Make sure to use a UNIQUE username '
                                    'and that your passwords match!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginUser(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            username = User.objects.get(email=email.lower()).username
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Welcome Back!')
            else:
                print('sad!')
                messages.error(request, 'Authentication Error: Email or password is invalid')
        except:
            messages.error(request, 'Authentication Error: Email or password is invalid')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkoutUser(request):
    pass
