"""
Defines a Django form for creating and updating instances of the UserModel model.

This form allows users to input data for various fields including user name, password, email, phone, and address.
Additionally, it provides custom validation to ensure the uniqueness of the user name and email fields.

Attributes:
    UserModelForm: A subclass of forms.ModelForm representing the form for UserModel model.
"""
from django import forms
from .models import PackagesModel, PackageDateModel, PackagePlanModel, TravelTipsModel


class UserModelForm(forms.ModelForm):
    class Meta:
        model = PackagesModel
        fields = ['packages_id','price', 'package_name', 'nation', 'no_of_bookings', 'start_date','end_date','package_image','description','total_days']

        # labels = {
        #     'price': 'Price',
        #     'user_password': 'Password',
        #     'user_email': 'Email',
        # }

        widgets = {
            'packages_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'package_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nation': forms.Select(attrs={'class': 'form-control'}),  # Foreign key dropdown
            'no_of_bookings': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'package_image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'total_days': forms.NumberInput(attrs={'class': 'form-control'}),

        }
class Packagedateform(forms.ModelForm):
    class Meta:
        model = PackageDateModel
        fields =['date_id','start_date','end_date','package']
        widgets = {
            'date_id': forms.NumberInput(attrs={'class': 'form-control'}),
           'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'package': forms.Select(attrs={'class': 'form-control'}),  # Foreign key dropdown
        }
class packageplanform(forms.ModelForm):
    class Meta:
        model = PackagePlanModel
        fields =['plan_id','oder','no_of_days','heading','description','package']
        widgets = {
            'plan_id': forms.NumberInput(attrs={'class': 'form-control'}),
           'oder': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'package': forms.Select(attrs={'class': 'form-control'}),
        }
class traveltipsform(forms.ModelForm):
    class Meta:
     model = TravelTipsModel
     fields = ['tips_id', 'nation', 'currency', 'climate', 'clothing', 'food','public_transport','shopping']
     widgets = {
        'tips_id': forms.NumberInput(attrs={'class': 'form-control'}),
        'nation': forms.Select(attrs={'class': 'form-control'}),
        'currency': forms.TextInput(attrs={'class': 'form-control'}),
        'climate': forms.TextInput(attrs={'class': 'form-control'}),
        'clothing': forms.TextInput(attrs={'class': 'form-control'}),
        'food': forms.TextInput(attrs={'class': 'form-control'}),
        'public_transport': forms.TextInput(attrs={'class': 'form-control'}),
       'shopping': forms.TextInput(attrs={'class': 'form-control'}),
    }