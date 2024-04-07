from django.shortcuts import render
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from .form import UserModelForm, Packagedateform, packageplanform, traveltipsform, nationform, NationImageform
from .models import *
# Create your views here.
def user_list(request):
    """
    Retrieves all user objects and renders them in the home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the home.html template with users' data.
    """
    packages = PackagesModel.objects.all()
    return render(request, 'admin_package_home.html', {'users': packages})
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
        form_obj = UserModelForm(request.POST,request.FILES)
        print(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print('form submit')
            return redirect('/Package_admin')
    else:
        form_obj = UserModelForm()
    return render(request, 'admin_package_regis.html', {'form': form_obj})
def update_packages_view(request, packages_id):
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
    user = PackagesModel.objects.get(packages_id=packages_id)
    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=user)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("user data updated...................")
    else:
        form = UserModelForm(instance=user)
    return render(request, 'admin_package_update.html', {'form': form})
def packagedate_home(request):
    """
    Retrieves all user objects and renders them in the home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the home.html template with users' data.
    """
    packages = PackageDateModel.objects.all()
    return render(request, 'admin_packdate_home.html', {'users': packages})
def date_registration(request):
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
        form_obj = Packagedateform(request.POST)
        print(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print('form submit')
            return redirect('/packages_dates')
    else:
        form_obj = Packagedateform()
    return render(request, 'admin_package_regis.html', {'form': form_obj})
def update_date_view(request, date_id):
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
    user = PackageDateModel.objects.get(date_id=date_id)
    if request.method == 'POST':
        form = Packagedateform(request.POST, instance=user)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("package date  updated...................")
    else:
        form = Packagedateform(instance=user)
    return render(request, 'admin_package_update.html', {'form': form})
def PackagePlan_home(request):
    """
    Retrieves all user objects and renders them in the home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the home.html template with users' data.
    """
    packages = PackagePlanModel.objects.all()
    return render(request, 'admin_packageplan_home.html', {'users': packages})
def plan_registration(request):
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
        form_obj = packageplanform(request.POST)
        print(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print('form submit')
            return redirect('/PackagePlan_home')
    else:
        form_obj = packageplanform()
    return render(request, 'admin_package_regis.html', {'form': form_obj})
def update_plan_view(request, plan_id):
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
    user =PackagePlanModel.objects.get(plan_id=plan_id)
    if request.method == 'POST':
        form = packageplanform(request.POST, instance=user)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("plan data updated...................")
    else:
        form = packageplanform(instance=user)
    return render(request, 'admin_package_update.html', {'form': form})
def traveltips_home(request):
    """
    Retrieves all user objects and renders them in the home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the home.html template with users' data.
    """
    tips = TravelTipsModel.objects.all()
    return render(request, 'admin_traveltips_home.html', {'users': tips})
def tips_registration(request):
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
        form_obj = traveltipsform(request.POST)
        print(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print('form submit')
            return redirect('/traveltips_home')
    else:
        form_obj = traveltipsform()
    return render(request, 'admin_package_regis.html', {'form': form_obj})
def update_tips_view(request, tips_id):
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
    user =TravelTipsModel.objects.get(tips_id=tips_id)
    if request.method == 'POST':
        form = traveltipsform(request.POST, instance=user)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("plan data updated...................")
    else:
        form = traveltipsform(instance=user)
    return render(request, 'admin_package_update.html', {'form': form})
def Nation_home(request):
    """
    Retrieves all user objects and renders them in the home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the home.html template with users' data.
    """
    nation = NationModel.objects.all()
    return render(request, 'admin_nation_home.html', {'users': nation})
def nation_registration(request):
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
        form_obj = nationform(request.POST)
        print(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print('form submit')
            return redirect('/nation')
    else:
        form_obj = nationform()
    return render(request, 'admin_package_regis.html', {'form': form_obj})
def update_nation_view(request, nation_id):
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
    user =NationModel.objects.get(nation_id=nation_id)
    if request.method == 'POST':
        form = nationform(request.POST, instance=user)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("plan data updated...................")
    else:
        form = nationform(instance=user)
    return render(request, 'admin_package_update.html', {'form': form})
def Nationimage_home(request):
    """
    Retrieves all user objects and renders them in the home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the home.html template with users' data.
    """
    nationimage = NationImageModel.objects.all()
    return render(request, 'admin_nationimage_home.html', {'users': nationimage})
def nationimage_registration(request):
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
        form_obj = NationImageform(request.POST,request.FILES)
        print(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print('form submit')
            return redirect('/nation_image')
    else:
        form_obj = NationImageform()
    return render(request, 'admin_package_regis.html', {'form': form_obj})
def update_nationimage_view(request, nation_image_id):
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
    user = NationImageModel.objects.get(nation_image_id=nation_image_id)
    if request.method == 'POST':
        form = NationImageform(request.POST, instance=user)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("user data updated...................")
    else:
        form = NationImageform(instance=user)
    return render(request, 'admin_package_update.html', {'form': form})
def admin_home(request):
    return render(request, 'admin_home.html')