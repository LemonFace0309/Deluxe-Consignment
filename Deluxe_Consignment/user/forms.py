from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

        # error messages like (passwords do not match) do not show as forms are either hardcoded into HTML or because
        # a modal is being used instead of a new page.
        # Therefore, no new form is automatically begin regenerated after error

