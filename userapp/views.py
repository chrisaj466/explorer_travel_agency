from datetime import date, datetime

from django.contrib import messages
from django.contrib.auth.models import User



import mysql
from django.db.models import Q, Sum, Count

from django.shortcuts import render, redirect,HttpResponse, get_object_or_404

from adminapp.models import PackageDateModel
from .models import PackagesModel, NationModel, NationImageModel, PackagePageModel, ReviewModel, TravelTipsModel, \
    PackagePlanModel, UserModel, UserImageModel, PaymentTypeModel, UserPaymentModel


# Create your views here.
def home(request):
    data = PackagesModel.objects.filter(nation_id=1)
    data2 = NationModel.objects.filter(nation_id=1)
    nations = NationModel.objects.all()
    # nation_names = [obj.nation_name for obj in nations]
    # print(nation_names)
    if request.session.get('user'):
        if request.session.get('nation'):
           nation=request.session.get('nation')
           data = PackagesModel.objects.filter(nation_id=nation)
           data2=NationModel.objects.filter(nation_id=nation)
           return render(request, 'home.html', {"DATA": data,'data2': data2,"category":nations})
        return render(request, 'home.html',{"DATA": data,'data2': data2,"category":nations})
    return render(request, 'home.html',{"DATA": data,'data2': data2,"category":nations})

def search(request):
    data1 = PackagesModel.objects.all()
    sort_data = None
    category_data = None
    search_data = ''
    nations = NationModel.objects.all()
    if request.method == 'POST':
        search_data = request.POST.get('search','')
        sort_data = request.POST.get('sort-select')
        category_data = request.POST.get('category-select')
        if category_data :
            print(category_data)
            data1=data1.filter(nation__nation_name__icontains=category_data)
            print(data1.values)
        if search_data:
            data1 = data1.filter(
                Q(nation__nation_name__icontains=search_data) |
                Q(total_days__icontains=search_data) |
                Q(package_name__icontains=search_data) |
                Q(price__icontains=search_data) |
                Q(start_date__icontains=search_data) |
                Q(end_date__icontains=search_data)
            )

        if sort_data == "small":
            data1 = data1.order_by('price')
        else:
            data1 = data1.order_by('-price')
        if not data1.exists():
            return redirect('/')
    return render(request, 'search_page.html',{'DATA':data1,"search_data":search_data,"category_data":category_data,"category":nations,'search':sort_data})
    # return redirect('/search_page')

def user_profile(request):
    if request.session.get('user'):
       user=request.session.get('user')
       user_model=UserModel.objects.get(User_name=user)
       user_login_id=user_model.User_id
       user_login=UserImageModel.objects.filter(user=user_login_id)
       return render(request, 'user_profile.html',{"user": user_login})
    return redirect('/login')
def contact(request):
    return render(request, 'contact.html')
def destination(request):
    DATA = NationImageModel.objects.all()
    return render(request, 'destination.html', {"data": DATA})
def forgot(request):
    return render(request, 'forgotpassword.html')
def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password=request.POST.get('password')
        user = UserModel.objects.get(email=email)
        user_id=user.User_id
        user_object =  UserModel.objects.get(User_id=user_id)
        user_object.Password=password
        user_object.save()
        return redirect('/login')
    return render(request, 'forgotpassword.html')
def profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('new-name')
        password = request.POST.get('new-password')
        email = request.POST.get('new-email')
        phone_number = request.POST.get('new-phone-number')
        status = 'active'
        user = request.session.get('user')
        print(user)
        user_model = UserModel.objects.get(User_name=user)
        print(user_model)
        user_id = user_model.User_id
        profile_obj =UserModel.objects.get(User_id=user_id)
        profile_obj.User_name = username
        profile_obj.Password = password
        profile_obj.Email = email
        profile_obj.Phone_number = phone_number
        profile_obj.Status = status

        print('hi')
        profile_obj.save()
        return redirect('/login')
    return redirect('/user_profile')
# def profile_update(request):
#     user_profile = UserImageModel.objects.get(user=request.user)
#     if request.method == 'POST':
#         user_profile.user.User_name = request.POST.get('new-name')
#         user_profile.user.Password = request.POST.get('new-password')
#         user_profile.user.Phone_number = request.POST.get('new-phone-number')
#         user_profile.user.email = request.POST.get('new-email')
#         status = 'active'
#         user_profile.user.status=status
#         if request.FILES.get('new-image'):
#             user_profile.image = request.FILES['new-image']
#
#         user_profile.user.save()  # Save the updated user information
#         user_profile.save()  # Save the UserProfile instance
#         messages.success(request, 'Your profile has been updated successfully.')
#         return redirect('/user_profile')  # Redirect to the user profile page
#     return redirect('/profile_update')
def about(request):
    return render(request, 'about.html')
def packages(request):
    DATA = NationImageModel.objects.all()
    return render(request, 'packages.html', {"data": DATA})


def countries_contents(request):
    id=request.POST.get('nation_image_id')
    data = NationImageModel.objects.filter(nation_image_id=id)
    print(data.values)
    return render(request, 'countries_contents.html', {'data': data})


def country_packages(request):
   if request.method == 'POST':
         request.session['nation']=request.POST.get('nation_image_id')
         nation_image_id = request.POST.get('nation_image_id')
         data = PackagesModel.objects.filter(nation_id=nation_image_id )
         data2 = NationModel.objects.filter(nation_id=nation_image_id )
         data3 = UserModel.objects.all()
         return render(request, 'country_packages.html', {'data': data, 'data2': data2})
   return redirect('/packages')

def package_plan(request):
    if request.method == 'POST':
        id=request.POST.get('packages_id')
        request.session['package_id'] = id
        data = PackagePlanModel.objects.filter(package_id=id).order_by('oder')
        data2=PackagesModel.objects.filter(packages_id=id)
        username=request.session['user']
        print(username)
        data3=ReviewModel.objects.filter(packages_id=id)
        total_rating_sum = data3.aggregate(total_sum=Sum('rating_value'))['total_sum']
        total_rating_count = data3.aggregate(total_count=Count('rating_value'))['total_count']
        print(int(total_rating_sum))
        print(int(total_rating_count))
        average_rating=total_rating_sum / total_rating_count
        print(average_rating)
        return render(request, 'package_plan.html', {'data': data,'data2': data2,'data3': data3,'average_rating': average_rating})
    return redirect('/country_packages')

def traveltips(request):
    DATA = NationImageModel.objects.all()
    return render(request, 'Traveltips.html', {"data": DATA})


def country_traveltips(request):
    id=request.POST.get('nation_image_id')
    data = TravelTipsModel.objects.filter(nation_id=id)
    data2 = NationModel.objects.filter(nation_id=id)
    return render(request, 'country_traveltip.html', {'data': data, 'data2': data2})


def booking(request):
    payment_provider=PaymentTypeModel.objects.all()
    if request.session.get('user'):
        print('log in')
        print(request.session['user'])
        return render(request, 'booking.html',{'payment_provider': payment_provider})

    return redirect('/login')
def userpayment(request):
    package_date = PackageDateModel.objects.filter(package=request.session.get('package_id'))
    if request.method=='POST':
        category_id=request.POST.get('category')
        provider=request.POST.get('provider')
        account_number=request.POST.get('account_number')
        expiry_date = request.POST.get('expiry_date')

        user=request.session.get('user')
        user_info=UserModel.objects.get(User_name=user)
        id=user_info.User_id
        print(id)
        obj=UserPaymentModel()
        obj.provider=provider
        obj.account_number=account_number
        obj.expiry_date=expiry_date
        obj.user_id=id
        users=UserModel.objects.get(User_id=id)
        print(users.User_name)
        obj.payment_type=PaymentTypeModel.objects.get(type_id=request.POST.get('category'))
        obj.save()
        date_time=UserPaymentModel.objects.get()
        return render(request, 'booking_list.html',{'package_date': package_date})
    return render(request,'booking.html')
def booking_list(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user=request.session.get('user')
        package=request.session.get('package_id')
        dat_time=request.POST.get('dat_time')
        payment=UserPaymentModel.objects.get(user=user, package=package)
        print(payment)
        return redirect('/package_plan')
    return render(request, 'booking_list.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserModel.objects.filter(User_name=username, Password=password)
        print(user.values())
        if user:
            print('login into the page is successful')
            request.session['user'] = username
            return redirect('/')
    return render(request, 'login.html')


def logout(request):
    del request.session['user']
    if request.session.get('nation'):
     del request.session['nation']
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('Phone_number')
        status = 'active'
        obj1 = UserModel()
        obj1.User_name = username
        obj1.Password = password
        obj1.Phone_number = phone_number
        obj1.email = email
        obj1.status = status
        obj1.save()
        return redirect('/')
    return render(request, 'register.html')
#
