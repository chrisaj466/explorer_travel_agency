from django.db import models


# Create your models here.
class NationModel(models.Model):
    nation_id = models.IntegerField(primary_key=True)
    nation_name = models.CharField(max_length=255)
    nation_description = models.TextField(null=True)
    def __str__(self):
        return self.nation_name
    class Meta:
        db_table = 'nation_table'



class NationImageModel(models.Model):
    nation_image_id = models.IntegerField(primary_key=True)
    nation_image = models.ImageField(upload_to='nation/')
    nation_id = models.ForeignKey(NationModel, on_delete=models.CASCADE)
    travel_tip_main_image = models.ImageField(upload_to='countrycontent',null=True)
    package_main_image = models.ImageField(upload_to='countrycontent',null=True)

    class Meta:
        db_table = 'nation_image'


class PackagesModel(models.Model):
    packages_id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    package_name = models.CharField(max_length=255)
    nation = models.ForeignKey(NationModel, on_delete=models.CASCADE)
    no_of_bookings = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    package_image = models.ImageField(upload_to='packages/')
    description = models.CharField(max_length=255)
    total_days=models.IntegerField(null=True)

    def __str__(self):
        return self.package_name
    class Meta:
        db_table = 'packages'
class PackageDateModel(models.Model):
    date_id=models.IntegerField(primary_key=True)
    start_date = models.DateField()
    count = models.IntegerField(default=10)
    package = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'packagedate'
class PackagePlanModel(models.Model):
    plan_id = models.IntegerField(primary_key=True)
    oder = models.IntegerField()
    no_of_days = models.IntegerField()
    heading=models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255)
    package = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)


    class Meta:
        db_table = 'package_plan'

class PackagePageModel(models.Model):
    page_id = models.IntegerField(primary_key=True)
    nation_id = models.ForeignKey(NationModel, on_delete=models.CASCADE)
    Nation_name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='packagepage/')


    def __str__(self):
        return self.Nation_name
    class Meta:
        db_table = 'package_page_images'

class TravelTipsModel(models.Model):
    tips_id = models.IntegerField(primary_key=True)
    nation = models.ForeignKey(NationModel, on_delete=models.CASCADE)
    currency = models.TextField()
    climate = models.TextField()
    clothing = models.TextField()
    food = models.TextField()
    public_transport = models.TextField()
    shopping = models.TextField()

    class Meta:
        db_table = 'travel_tips'
class PaymentModel(models.Model):
    payment_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)
    user = models.CharField(max_length=255, null=True)
    package = models.CharField(max_length=255, null=True)
    members = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    start_date = models.DateField(null=True)
    class Meta:
        db_table = 'payment_home'