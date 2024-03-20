from django.apps import AppConfig
from django.contrib import admin

class ExplorerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userapp'
    def ready(self):
        from .models import UserModel,UserImageModel,PaymentTypeModel,UserPaymentModel,BookingListModel,ReviewModel
        admin.site.register(UserModel)
        admin.site.register(UserImageModel)
        admin.site.register(PaymentTypeModel)
        admin.site.register(UserPaymentModel)
        admin.site.register(BookingListModel)
        admin.site.register(ReviewModel)