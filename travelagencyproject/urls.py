"""
URL configuration for travelagencyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userapp import views as user_views
from adminapp import views as admin_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.home,name='home'),

    #payment


    # packages model
    path('Package_admin', admin_views.user_list),
    path('registration', admin_views.registration),
    path('update/<int:packages_id>/',admin_views.update_packages_view),

    # packages dates model
    path('packages_dates', admin_views.packagedate_home),
    path('date_registration', admin_views.date_registration),
    path('date_update/<int:date_id>/',admin_views.update_date_view),

    #packages plan model
    path('PackagePlan_home', admin_views.PackagePlan_home),
    path('plan_registration', admin_views.plan_registration),
    path('plan_update/<int:plan_id>/', admin_views.update_plan_view),

    #traveltips model
    path('traveltips_home', admin_views.traveltips_home),
    path('tips_registration', admin_views.tips_registration),
    path('tips_update/<int:tips_id>/', admin_views.update_tips_view),

    # search option
    path('search_page',user_views.search,name='search_page'),

    #booking
    # path('booking',user_views.booking,name='booking'),

    #userpayment
    # path('userpayment',user_views.userpayment,name='userpayment'),

    #booking_list
    # path('booking_list',user_views.booking_list,name='booking_list'),

    #payment
    path('initiate_payment', user_views.initiate_payment, name='initiate_payment'),
    path('payment', user_views.payment, name='payment'),
    path('payment_success', user_views.payment_success, name='payment_success'),
    path('payment_failure', user_views.payment_failure, name='payment_failure'),


    path('user_profile',user_views.user_profile,name='user_profile'),
    path('destination', user_views.destination,name='destination'),
    path('packages', user_views.packages,name='packages'),
    # path('booking', user_views.booking,name='booking'),
    path('login', user_views.login,name='login'),
    path('logout', user_views.logout, name='logout'),
    path('profile_update', user_views.profile_update,name='profile_update'),
    path('register', user_views.register, name='register'),
    path('forgot', user_views.forgot, name='forgot'),
    path('contact', user_views.contact, name='contact'),
    path('forgotpassword',user_views.forgotpassword,name='forgotpassword'),
    path('about', user_views.about, name='about'),
    path('Traveltips', user_views.traveltips,name='traveltips'),
    path('countries_contents', user_views.countries_contents,name='countries_contents'),
    path('country_packages',user_views.country_packages,name='country_packages'),
    path('package_plan', user_views.package_plan,name='package_plan'),
    path('country_traveltip', user_views.country_traveltips, name='country_traveltip'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
