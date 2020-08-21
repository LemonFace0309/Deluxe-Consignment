from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from . forms import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
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
            else:
                messages.error(request, 'Authentication Error: Email or password is incorrect')
        except:
            messages.error(request, 'Authentication Error: Email or password is incorrect')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
