from django.shortcuts import render
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404

from userapp.models import Payment
# from userapp.models import Payment
from .form import UserModelForm, Packagedateform, packageplanform, traveltipsform, nationform, NationImageform
from .models import *
from django.db.models import Sum
from django.db.models import Count
# Create your views here.
def user_list(request):
    """
    Retrieves all package objects and renders them in the admin_package_home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_package_home.html template with package data.
    """
    packages = PackagesModel.objects.all()
    return render(request, 'admin_package_home.html', {'users': packages})
def registration(request):
    """
    Handles package registration, validating and saving form data.

    If the request method is GET, renders an empty registration form.
    If the request method is POST, validates the submitted form data.
    If the form is valid, saves the data and redirects to the admin_package_home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the reg_validation.html template with the registration form.
    - Redirects to the admin_package_home page on successful registration.
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
    Handles updating package information based on packages_id.

    If the request method is GET, renders a form pre-populated with packages existing data.
    If the request method is POST, validates the submitted form data.
    If the form is valid, updates the package information and returns a success message.

    Parameters:
    - request: HttpRequest object.
    - packages_id: Integer specifying the packages_id ID.

    Returns:
    - HttpResponse object rendering the admin_package_update template with the form.
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
    Retrieves all package date objects and renders them in the admin_packdate_home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_packdate_home.html template with users' data.
    """
    packages = PackageDateModel.objects.all()
    return render(request, 'admin_packdate_home.html', {'users': packages})
def date_registration(request):
    """
    Handles package date registration, validating and saving form data.

    If the request method is GET, renders an empty registration form.
    If the request method is POST, validates the submitted form data.
    If the form is valid, saves the data and redirects to the admin_packdate_home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_package_regis.html template with the registration form.
    - Redirects to the admin_packdate_home page on successful registration.
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
    Handles updating package date information based on date_id.

    If the request method is GET, renders a form pre-populated with package date existing data.
    If the request method is POST, validates the submitted form data.
    If the form is valid, updates the user's information and returns a success message.

    Parameters:
    - request: HttpRequest object.
    - date_id: Integer specifying the date ID.

    Returns:
    - HttpResponse object rendering the admin_package_update.html template with the form.
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
    Retrieves all PackagePlan objects and renders them in the admin_packageplan_home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_packageplan_home.html template with PackagePlan data.
    """
    packages = PackagePlanModel.objects.all()
    return render(request, 'admin_packageplan_home.html', {'users': packages})
def plan_registration(request):
    """
    Handles PackagePlan registration, validating and saving form data.

    If the request method is GET, renders an empty registration form.
    If the request method is POST, validates the submitted form data.
    If the form is valid, saves the data and redirects to the admin_packageplan_home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_package_regis.html template with the registration form.
    - Redirects to the admin_packageplan_home page on successful registration.
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
    Handles updating plan information based on plan_id.

    If the request method is GET, renders a form pre-populated with plan  existing data.
    If the request method is POST, validates the submitted form data.
    If the form is valid, updates the update_plan information and returns a success message.

    Parameters:
    - request: HttpRequest object.
    - plan_id: Integer specifying the plan ID.

    Returns:
    - HttpResponse object rendering the admin_package_update.html template with the form.
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
    Retrieves all traveltips objects and renders them in the admin_traveltips_home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_traveltips_home.html template with traveltips data.
    """
    tips = TravelTipsModel.objects.all()
    return render(request, 'admin_traveltips_home.html', {'users': tips})
def tips_registration(request):
    """
    Handles traveltips registration, validating and saving form data.

    If the request method is GET, renders an empty registration form.
    If the request method is POST, validates the submitted form data.
    If the form is valid, saves the data and redirects to the admin_traveltips_home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_package_regis.html template with the registration form.
    - Redirects to the admin_traveltips_home page on successful registration.
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
    Handles updating traveltips information based on  tips_id.

    If the request method is GET, renders a form pre-populated with traveltips existing data.
    If the request method is POST, validates the submitted form data.
    If the form is valid, updates the user's information and returns a success message.

    Parameters:
    - request: HttpRequest object.
    -  tips_id: Integer specifying the  tips ID.

    Returns:
    - HttpResponse object rendering the admin_package_update.htm template with the form.
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
    Retrieves all Nation objects and renders them in the admin_nation_home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_nation_home.html template with Nation data.
    """
    nation = NationModel.objects.all()
    return render(request, 'admin_nation_home.html', {'users': nation})
def nation_registration(request):
    """
    Handles Nation registration, validating and saving form data.

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
    Handles updating nation information based on nation_id.

    If the request method is GET, renders a form pre-populated with nation existing data.
    If the request method is POST, validates the submitted form data.
    If the form is valid, updates the nation_id information and returns a success message.

    Parameters:
    - request: HttpRequest object.
    - nation_id: Integer specifying the nation ID.

    Returns:
    - HttpResponse object rendering the admin_package_update.html template with the form.
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
    Retrieves all Nationimage objects and renders them in the admin_nationimage_home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_nationimage_home.html template with Nationimage data.
    """
    nationimage = NationImageModel.objects.all()
    return render(request, 'admin_nationimage_home.html', {'users': nationimage})
def nationimage_registration(request):
    """
    Handles nationimage registration, validating and saving form data.

    If the request method is GET, renders an empty registration form.
    If the request method is POST, validates the submitted form data.
    If the form is valid, saves the data and redirects to the home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_package_regis.html template with the registration form.
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
    Handles updating nationimage information based on  nation_image_id.

    If the request method is GET, renders a form pre-populated with nationimage existing data.
    If the request method is POST, validates the submitted form data.
    If the form is valid, updates the user's information and returns a success message.

    Parameters:
    - request: HttpRequest object.
    - nation_image_id: Integer specifying the nation_image ID.

    Returns:
    - HttpResponse object rendering the admin_package_update.html template with the form.
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


def Payment_home(request):
    """
    Retrieves all Payment objects and renders them in the admin_payment_home.html template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the admin_payment_home.html template with Payment data.
    """
    Payment = PaymentModel.objects.all()
    return render(request, 'admin_payment_home.html', {'users': Payment})






















# def admin_home(request):
#
#     total_price = Payment.objects.aggregate(total_price=Sum('price'))
#     total_bookings_count = Payment.objects.aggregate(total_bookings_count=Count('id'))
#     # Extract start dates and prices
#     prices = Payment.objects.values_list('price', flat=True)  # Query price data from the Payment model
#     prices_string = ",".join(str(price) for price in prices)
#
#     context = {
#         'total_price': total_price,'total_bookings_count': total_bookings_count,'prices_string': prices_string
#     }
#     return render(request, 'admin_home.html',context)




def admin_home(request):
    # Get total price and count of payments
    total_price = Payment.objects.aggregate(total_price=Sum('price'))
    total_bookings_count = Payment.objects.aggregate(total_bookings_count=Count('id'))

    # Extract created_at dates and prices
    earnings_data = Payment.objects.values_list('created_at', 'price')  # Query created_at and price data from the Payment model

    # Extract month names and corresponding earnings
    month_earnings = {}
    for date, price in earnings_data:
        month = date.strftime("%b")  # Get abbreviated month name
        if month not in month_earnings:
            month_earnings[month] = 0
        month_earnings[month] += price

    # Create lists for chart labels and data
    labels = list(month_earnings.keys())
    earnings = list(month_earnings.values())

    context = {
        'total_price': total_price,
        'total_bookings_count': total_bookings_count,
        'labels': labels,
        'earnings': earnings
    }
    return render(request, 'admin_home.html', context)
