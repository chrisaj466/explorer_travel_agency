from django.db import models


# Create your models here.
# The NationModel class defines the model for representing nations in the database.
# It contains fields for the nation ID, name, and description.

class NationModel(models.Model):
    # The nation_id field serves as the primary key for the nation.
    nation_id = models.IntegerField(primary_key=True)

    # The nation_name field stores the name of the nation.
    nation_name = models.CharField(max_length=255)

    # The nation_description field stores a description of the nation, allowing for null values.
    nation_description = models.TextField(null=True)

    # The __str__ method returns the nation name when the object is converted to a string.
    def __str__(self):
        return self.nation_name

    # The Meta class provides metadata for the NationModel class, specifying the database table name.
    class Meta:
        db_table = 'nation_table'


# The NationImageModel class defines the model for representing images associated with nations in the database.
# It contains fields for the nation image ID, image file, associated nation ID, travel tip main image, and package main image.

class NationImageModel(models.Model):
    # The nation_image_id field serves as the primary key for the nation image.
    nation_image_id = models.IntegerField(primary_key=True)

    # The nation_image field stores the image file for the nation.
    nation_image = models.ImageField(upload_to='nation/')

    # The nation_id field is a foreign key that associates the image with a specific nation.
    nation_id = models.ForeignKey(NationModel, on_delete=models.CASCADE)

    # The travel_tip_main_image field stores the main image for travel tips associated with the nation, allowing for null values.
    travel_tip_main_image = models.ImageField(upload_to='countrycontent', null=True)

    # The package_main_image field stores the main image for packages associated with the nation, allowing for null values.
    package_main_image = models.ImageField(upload_to='countrycontent', null=True)

    # The Meta class provides metadata for the NationImageModel class, specifying the database table name.
    class Meta:
        db_table = 'nation_image'


# The PackagesModel class defines the model for representing packages in the database.
# It contains fields for the package ID, price, name, associated nation, number of bookings,
# start and end dates, package image, description, and total days.

class PackagesModel(models.Model):
    # The packages_id field serves as the primary key for the package.
    packages_id = models.IntegerField(primary_key=True)

    # The price field stores the price of the package.
    price = models.IntegerField()

    # The package_name field stores the name of the package.
    package_name = models.CharField(max_length=255)

    # The nation field is a foreign key that associates the package with a specific nation.
    nation = models.ForeignKey(NationModel, on_delete=models.CASCADE)

    # The no_of_bookings field stores the number of bookings for the package.
    no_of_bookings = models.IntegerField()

    # The start_date field stores the start date of the package.
    start_date = models.DateField()

    # The end_date field stores the end date of the package.
    end_date = models.DateField()

    # The package_image field stores the image file for the package.
    package_image = models.ImageField(upload_to='packages/')

    # The description field stores a brief description of the package.
    description = models.CharField(max_length=255)

    # The total_days field stores the total number of days for the package, allowing for null values.
    total_days = models.IntegerField(null=True)

    # The __str__ method returns the package name when the object is converted to a string.
    def __str__(self):
        return self.package_name

    # The Meta class provides metadata for the PackagesModel class, specifying the database table name.
    class Meta:
        db_table = 'packages'


# The PackageDateModel class defines the model for representing dates associated with packages in the database.
# It contains fields for the date ID, start date, count, and associated package.

class PackageDateModel(models.Model):
    # The date_id field serves as the primary key for the date.
    date_id = models.IntegerField(primary_key=True)

    # The start_date field stores the start date associated with the package.
    start_date = models.DateField()

    # The count field stores the count associated with the package, with a default value of 10.
    count = models.IntegerField(default=10)

    # The package field is a foreign key that associates the date with a specific package.
    package = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)

    # The Meta class provides metadata for the PackageDateModel class, specifying the database table name.
    class Meta:
        db_table = 'packagedate'


# The PackagePlanModel class defines the model for representing plans associated with packages in the database.
# It contains fields for the plan ID, order, number of days, heading, description, and associated package.

class PackagePlanModel(models.Model):
    # The plan_id field serves as the primary key for the plan.
    plan_id = models.IntegerField(primary_key=True)

    # The order field specifies the order of the plan.
    oder = models.IntegerField()

    # The no_of_days field stores the number of days associated with the plan.
    no_of_days = models.IntegerField()

    # The heading field stores the heading or title of the plan, allowing for null values.
    heading = models.CharField(max_length=255, null=True)

    # The description field stores the description of the plan.
    description = models.CharField(max_length=255)

    # The package field is a foreign key that associates the plan with a specific package.
    package = models.ForeignKey(PackagesModel, on_delete=models.CASCADE)

    # The Meta class provides metadata for the PackagePlanModel class, specifying the database table name.
    class Meta:
        db_table = 'package_plan'


# The PackagePageModel class defines the model for representing page images associated with packages in the database.
# It contains fields for the page ID, associated nation ID, nation name, and image.

class PackagePageModel(models.Model):
    # The page_id field serves as the primary key for the page.
    page_id = models.IntegerField(primary_key=True)

    # The nation_id field is a foreign key that associates the page with a specific nation.
    nation_id = models.ForeignKey(NationModel, on_delete=models.CASCADE)

    # The Nation_name field stores the name of the nation associated with the page.
    Nation_name = models.CharField(max_length=255)

    # The image field stores the image file for the page.
    image = models.ImageField(upload_to='packagepage/')

    # The __str__ method returns the nation name when the object is converted to a string.
    def __str__(self):
        return self.Nation_name

    # The Meta class provides metadata for the PackagePageModel class, specifying the database table name.
    class Meta:
        db_table = 'package_page_images'


# The TravelTipsModel class defines the model for representing travel tips associated with nations in the database.
# It contains fields for the tips ID, associated nation, currency, climate, clothing, food, public transport, and shopping tips.

class TravelTipsModel(models.Model):
    # The tips_id field serves as the primary key for the travel tip.
    tips_id = models.IntegerField(primary_key=True)

    # The nation field is a foreign key that associates the travel tip with a specific nation.
    nation = models.ForeignKey(NationModel, on_delete=models.CASCADE)

    # The currency field stores information about the currency in the nation.
    currency = models.TextField()

    # The climate field stores information about the climate in the nation.
    climate = models.TextField()

    # The clothing field stores information about clothing recommendations for the nation.
    clothing = models.TextField()

    # The food field stores information about local food recommendations in the nation.
    food = models.TextField()

    # The public_transport field stores information about public transportation tips in the nation.
    public_transport = models.TextField()

    # The shopping field stores information about shopping tips in the nation.
    shopping = models.TextField()

    # The Meta class provides metadata for the TravelTipsModel class, specifying the database table name.
    class Meta:
        db_table = 'travel_tips'


# The PaymentModel class defines the model for representing payment details in the database.
# It contains fields for the payment ID, order ID, signature, user, package, members, price,
# creation date, and start date.

# class PaymentModel(models.Model):
#     # The payment_id field stores the unique identifier for the payment.
#     payment_id = models.CharField(max_length=100)
#
#     # The order_id field stores the unique identifier for the order.
#     order_id = models.CharField(max_length=100)
#
#     # The signature field stores the signature associated with the payment.
#     signature = models.CharField(max_length=100)
#
#     # The user field stores the user associated with the payment, allowing for null values.
#     user = models.CharField(max_length=255, null=True)
#
#     # The package field stores the package associated with the payment, allowing for null values.
#     package = models.CharField(max_length=255, null=True)
#
#     # The members field stores the number of members associated with the payment, allowing for null values.
#     members = models.IntegerField(null=True)
#
#     # The price field stores the price associated with the payment, allowing for null values.
#     price = models.IntegerField(null=True)
#
#     # The created_at field stores the date and time when the payment was created.
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#
#     # The start_date field stores the start date associated with the payment, allowing for null values.
#     start_date = models.DateField(null=True)
#
#     # The Meta class provides metadata for the PaymentModel class, specifying the database table name.
#     class Meta:
#         db_table = 'payment_home'
