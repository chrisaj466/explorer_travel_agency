# Generated by Django 5.0.2 on 2024-03-21 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_alter_packagesmodel_packages_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packagesmodel',
            old_name='nation_id',
            new_name='nation',
        ),
    ]
