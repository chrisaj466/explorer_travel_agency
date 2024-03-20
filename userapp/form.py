"""
Defines a Django form for creating and updating instances of the UserModel model.

This form allows users to input data for various fields including user name, password, email, phone, and address.
Additionally, it provides custom validation to ensure the uniqueness of the user name and email fields.

Attributes:
    UserModelForm: A subclass of forms.ModelForm representing the form for UserModel model.
"""
from django import forms
from .models import UserModel


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['User_name', 'Password', 'email', 'Phone_number', 'status']

        labels = {
            'user_name': 'Student Name',
            'user_password': 'Password',
            'user_email': 'Email',
        }

        widgets = {
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'User_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emai': forms.EmailInput(attrs={'class': 'form-control'}),
            'Phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control good-input', 'style': 'color: red;'}),
        }

    def clean_user_name(self):
        """
        Custom validation method to ensure the uniqueness of the user name.

        Raises:
            forms.ValidationError: If the user name already exists in the database.
        """
        user_name = self.cleaned_data.get('user_name')
        if UserModel.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")
        return user_name

    def clean_user_email(self):
        """
        Custom validation method to ensure the uniqueness of the email address.

        Raises:
            forms.ValidationError: If the email address already exists in the database.
        """
        user_email = self.cleaned_data.get('user_email')
        if UserModel.objects.filter(user_email=user_email).exists():
            raise forms.ValidationError("Email address already exists. Please use a different one.")
        return user_email
