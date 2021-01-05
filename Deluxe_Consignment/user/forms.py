from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import *


# raise validationerrors whenever you have time
class CreateUserForm(UserCreationForm):
    subscription = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

        # error messages like (passwords do not match) do not show as forms are either hardcoded into HTML or because
        # a modal is being used instead of a new page.
        # Therefore, no new form is automatically begin regenerated after error


class UpdateUserForm(ModelForm):
    cur_password = forms.CharField()
    phone = forms.CharField(max_length=12, required=False)
    password1 = forms.CharField(max_length=32, required=False)
    password2 = forms.CharField(max_length=32, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'type': 'email',
        'name': 'email'
        }))


class ShippingAddressForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    layaway = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'custom-control-input layaway'}), required=False)

    class Meta:
        model = ShippingAddress
        fields = "__all__"
        exclude = ['customer', 'order']

        widgets = {
            'address': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "1234 Main St"
            }),
            'address2': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Apartment or suite"
            }),
            'city': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "City or Suburb"
            }),
            'country': forms.Select(attrs={
                'class': "form-control"
            }),
            'province': forms.Select(attrs={
                'class': "form-control",
            }),
            'postal_code': forms.TextInput(attrs={
                'class': "form-control"
            }),
        }


class PickUpForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    layaway2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'custom-control-input layaway'}), required=False)


class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = ['code']

        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Promo code',
                'aria-label': 'Recipient\'s username',
                'aria-describedby': 'basic-addon2'
            })
        }


class EmailSignupForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'id': "defaultSubscriptionFormPassword",
        'class': "form-control mb-4",
        'placeholder': "Name"
    }), label="", required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'id': "defaultSubscriptionFormEmail",
        'class': "form-control mb-4",
        'placeholder': "E-Mail"
    }), label="")

    class Meta:
        model = EmailSignup
        fields = ['name', 'email']
