from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

        # error messages like (passwords do not match) do not show as forms are either hardcoded into HTML or because
        # a modal is being used instead of a new page.
        # Therefore, no new form is automatically begin regenerated after error


class ShippingAddressForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)

    class Meta:
        model = ShippingAddress
        fields = "__all__"
        exclude = ['customer', 'order']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control"
            }),
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
