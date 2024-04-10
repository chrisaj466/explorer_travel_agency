from django.apps import AppConfig
from django.contrib import admin

class AdminappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminapp'
    def ready(self):
        from .models import  NationModel, NationImageModel,PackagesModel,PackagePlanModel,TravelTipsModel,PackageDateModel,PackagePageModel,PaymentModel
        admin.site.register(NationModel)
        admin.site.register(NationImageModel)
        admin.site.register(PackagesModel)
        admin.site.register(PackagePlanModel)
        admin.site.register(TravelTipsModel)
        admin.site.register(PackageDateModel)
        admin.site.register(PackagePageModel)
        admin.site.register(PaymentModel)

