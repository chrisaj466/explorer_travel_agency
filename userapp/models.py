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
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_image'



class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)
    user = models.CharField(max_length=255, null=True)
    package = models.CharField(max_length=255, null=True)
    members = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'payment'


class MapArea(models.Model):
    coordinates = models.CharField(max_length=50)
    nation_id = models.IntegerField()  # Assuming nation is represented by an integer ID

    def __str__(self):
        return f"Coordinates: {self.coordinates}, Nation: {self.nation_id}"

    class Meta:
        db_table = 'area_table'





class ReviewModel(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    packages = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)
    rating_value = models.CharField(max_length=255)
    comment = models.TextField()
    user_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'review'
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    class Meta:
        db_table = 'contact'