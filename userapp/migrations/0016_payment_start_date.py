# Generated by Django 5.0.2 on 2024-03-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_payment_alter_userpaymentmodel_package_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
