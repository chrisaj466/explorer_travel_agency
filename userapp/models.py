from django.db import models
from adminapp.models import *


# Create your models here.

class UserModel(models.Model):
    User_id = models.AutoField(primary_key=True)
    User_name = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_table'


class UserImageModel(models.Model):
    image_id = models.AutoField(primary_key=True)
    images = models.ImageField(upload_to='')
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_image'


class PaymentTypeModel(models.Model):
    type_id = models.IntegerField(primary_key=True)
    payment_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'payment_type'


class UserPaymentModel(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(PaymentTypeModel, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    expiry_date = models.DateField()

    class Meta:
        db_table = 'user_payment'


class BookingListModel(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    packages = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)
    payment = models.ForeignKey(UserPaymentModel, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255,default='Active')
    order_quantity = models.IntegerField()

    class Meta:
        db_table = 'booking_list'


class ReviewModel(models.Model):
    review_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    packages_id = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)
    rating_value = models.CharField(max_length=255)
    comment = models.TextField()
    user_name=models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'review'


# class BookingListModel(models.Model):
#     booking_id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     packages_id = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)
#     payment_id = models.ForeignKey(UserPaymentModel, on_delete=models.CASCADE)
#     order_status = models.CharField(max_length=255)
#     order_quantity = models.IntegerField()
#
#     class Meta:
#         db_table = 'booking_list'
