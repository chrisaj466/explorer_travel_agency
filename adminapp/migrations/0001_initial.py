# Generated by Django 5.0.2 on 2024-04-09 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NationModel',
            fields=[
                ('nation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nation_name', models.CharField(max_length=255)),
                ('nation_description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'nation_table',
            },
        ),
        migrations.CreateModel(
            name='payment_home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('order_id', models.CharField(max_length=100)),
                ('signature', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=255, null=True)),
                ('package', models.CharField(max_length=255, null=True)),
                ('members', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'payment_home',
            },
        ),
        migrations.CreateModel(
            name='NationImageModel',
            fields=[
                ('nation_image_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nation_image', models.ImageField(upload_to='nation/')),
                ('travel_tip_main_image', models.ImageField(null=True, upload_to='countrycontent')),
                ('package_main_image', models.ImageField(null=True, upload_to='countrycontent')),
                ('nation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.nationmodel')),
            ],
            options={
                'db_table': 'nation_image',
            },
        ),
        migrations.CreateModel(
            name='PackagePageModel',
            fields=[
                ('page_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Nation_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='packagepage/')),
                ('nation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.nationmodel')),
            ],
            options={
                'db_table': 'package_page_images',
            },
        ),
        migrations.CreateModel(
            name='PackagesModel',
            fields=[
                ('packages_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('package_name', models.CharField(max_length=255)),
                ('no_of_bookings', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('package_image', models.ImageField(upload_to='packages/')),
                ('description', models.CharField(max_length=255)),
                ('total_days', models.IntegerField(null=True)),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.nationmodel')),
            ],
            options={
                'db_table': 'packages',
            },
        ),
        migrations.CreateModel(
            name='PackagePlanModel',
            fields=[
                ('plan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('oder', models.IntegerField()),
                ('no_of_days', models.IntegerField()),
                ('heading', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.packagesmodel')),
            ],
            options={
                'db_table': 'package_plan',
            },
        ),
        migrations.CreateModel(
            name='PackageDateModel',
            fields=[
                ('date_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('count', models.IntegerField(default=10)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.packagesmodel')),
            ],
            options={
                'db_table': 'packagedate',
            },
        ),
        migrations.CreateModel(
            name='TravelTipsModel',
            fields=[
                ('tips_id', models.IntegerField(primary_key=True, serialize=False)),
                ('currency', models.TextField()),
                ('climate', models.TextField()),
                ('clothing', models.TextField()),
                ('food', models.TextField()),
                ('public_transport', models.TextField()),
                ('shopping', models.TextField()),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.nationmodel')),
            ],
            options={
                'db_table': 'travel_tips',
            },
        ),
    ]
