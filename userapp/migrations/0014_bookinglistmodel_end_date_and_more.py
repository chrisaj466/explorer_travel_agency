# Generated by Django 5.0.2 on 2024-03-27 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_userpaymentmodel_package_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinglistmodel',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookinglistmodel',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
