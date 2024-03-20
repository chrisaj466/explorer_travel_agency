from datetime import date, datetime

from django.contrib.auth.models import User



import mysql

from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from .form import UserModelForm
from .models import *

# from .models import PackagesModel, NationModel, NationImageModel, PackagePageModel, ReviewModel, TravelTipsModel, PackagePlanModel,UserModel
"""
Defines a Django form for creating and updating instances of the UserModel model.

This form allows users to input data for various fields including user name, password, email, phone, and address.
Additionally, it provides custom validation to ensure the uniqueness of the user name and email fields.

Attributes:
    UserModelForm: A subclass of forms.ModelForm representing the form for UserModel model.
"""

def user_list(request):
    """
    Retrieves all user objects and renders them in the home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the home.html template with users' data.
    """
    users = UserModel.objects.all()
    return render(request, 'home1.html', {'users': users})
def registration(request):
    """
    Handles user registration, validating and saving form data.

    If the request method is GET, renders an empty registration form.
    If the request method is POST, validates the submitted form data.
    If the form is valid, saves the data and redirects to the home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the reg_validation.html template with the registration form.
    - Redirects to the home page on successful registration.
    """
    if request.method == 'POST':
        form_obj = UserModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/')
    else:
        form_obj = UserModelForm()
    return render(request, 'reg_validation.html', {'form': form_obj})
def update_user_view(request, user_id):
    """
    Handles updating user information based on user_id.

    If the request method is GET, renders a form pre-populated with user's existing data.
    If the request method is POST, validates the submitted form data.
    If the form is valid, updates the user's information and returns a success message.

    Parameters:
    - request: HttpRequest object.
    - user_id: Integer specifying the user's ID.

    Returns:
    - HttpResponse object rendering the update_user.html template with the form.
    """
    user = UserModel.objects.get(User_id=user_id)
    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse("user data updated...................")
    else:
        form = UserModelForm(instance=user)
    return render(request, 'update_user.html', {'form': form})
# Create your views here.
# def home(request):
#     data = PackagesModel.objects.filter(nation_id=1)
#     data2 = NationModel.objects.filter(nation_id=1)
#     if request.session.get('user'):
#         if request.session.get('nation'):
#            nation=request.session.get('nation')
#            data = PackagesModel.objects.filter(nation_id=nation)
#            data2=NationModel.objects.filter(nation_id=nation)
#            return render(request, 'home.html', {"DATA": data,'data2': data2})
#         return render(request, 'home.html',{"DATA": data,'data2': data2})
#     return render(request, 'home.html',{"DATA": data,'data2': data2})
# def contact(request):
#     return render(request, 'contact.html')
# def destination(request):
#     DATA = NationImageModel.objects.all()
#     return render(request, 'destination.html', {"data": DATA})
# def forgot(request):
#     return render(request, 'forgotpassword.html')
# def forgotpassword(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password=request.POST.get('password')
#         user = UserModel.objects.get(email=email)
#         user_id=user.User_id
#         user_object =  UserModel.objects.get(User_id=user_id)
#         user_object.Password=password
#         user_object.save()
#         return redirect('/login')
#     return render(request, 'forgotpassword.html')
#
#
# def about(request):
#     return render(request, 'about.html')
# def packages(request):
#     DATA = NationImageModel.objects.all()
#     return render(request, 'packages.html', {"data": DATA})
#
#
# def countries_contents(request):
#     id=request.POST.get('nation_image_id')
#     data = NationImageModel.objects.filter(nation_image_id=id)
#     print(data.values)
#     return render(request, 'countries_contents.html', {'data': data})
#
#
# def country_packages(request):
#    if request.method == 'POST':
#          request.session['nation']=request.POST.get('nation_image_id')
#          nation_image_id = request.POST.get('nation_image_id')
#          data = PackagesModel.objects.filter(nation_id=nation_image_id )
#          data2 = NationModel.objects.filter(nation_id=nation_image_id )
#          data3 = UserModel.objects.all()
#          return render(request, 'country_packages.html', {'data': data, 'data2': data2})
#    return redirect('/packages')
#
# def package_plan(request):
#     if request.method == 'POST':
#         id=request.POST.get('packages_id')
#         data = PackagePlanModel.objects.filter(package_id=id).order_by('oder')
#         data2=PackagesModel.objects.filter(packages_id=id)
#         username=request.session['user']
#         print(username)
#         name=request.session['user']
#         review=ReviewModel.objects.filter(packages_id=id)
#         data3=review.filter(user_name=name)
#         print(data3.values)
#         return render(request, 'package_plan.html', {'data': data,'data2': data2,'data3': data3})
#     return redirect('/country_packages')
#
# def traveltips(request):
#     DATA = NationImageModel.objects.all()
#     return render(request, 'Traveltips.html', {"data": DATA})
#
#
# def country_traveltips(request):
#     id=request.POST.get('nation_image_id')
#     data = TravelTipsModel.objects.filter(nation_id=id)
#     data2 = NationModel.objects.filter(nation_id=id)
#     return render(request, 'country_traveltip.html', {'data': data, 'data2': data2})
#
#
# def booking(request):
#     if request.session.get('user'):
#         print('log in')
#         print(request.session['user'])
#
#     return redirect('/login')
#
#
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = UserModel.objects.filter(User_name=username, Password=password)
#         print(user.values())
#         if user:
#             print('login into the page is successful')
#             request.session['user'] = username
#             return redirect('/')
#     return render(request, 'login.html')
#
#
# def logout(request):
#     del request.session['user']
#     del request.session['nation']
#     return redirect('/')
#
#
# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('Phone_number')
#         status = 'active'
#         obj1 = UserModel()
#         obj1.User_name = username
#         obj1.Password = password
#         obj1.Phone_number = phone_number
#         obj1.email = email
#         obj1.status = status
#         obj1.save()
#         return redirect('/')
#     return render(request, 'register.html')
#
