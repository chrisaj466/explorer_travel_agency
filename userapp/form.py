# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from userapp.models import UserModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['User_name', 'Password', 'Phone_number', 'email']
        widgets = {
            'User_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }



