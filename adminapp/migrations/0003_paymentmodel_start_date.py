# Generated by Django 5.0.2 on 2024-04-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_rename_payment_home_paymentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmodel',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
