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
from django.urls import path
from userapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    # path('', views.user_list),
    # path('registration', views.registration),
    # path('update_user', views.update_user_view),
    # path('update/<int:user_id>/',views.update_user_view),
    #
    path('destination', views.destination,name='destination'),
    path('packages', views.packages,name='packages'),
    path('booking', views.booking,name='booking'),
    path('login', views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('forgot', views.forgot, name='forgot'),
    path('contact', views.contact, name='contact'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('about', views.about, name='about'),
    path('Traveltips', views.traveltips,name='traveltips'),
    path('countries_contents', views.countries_contents,name='countries_contents'),
    path('country_packages',views.country_packages,name='country_packages'),
    path('package_plan', views.package_plan,name='package_plan'),
    path('country_traveltip', views.country_traveltips, name='country_traveltip'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
