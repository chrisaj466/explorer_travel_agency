# Generated by Django 5.0.2 on 2024-03-22 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0021_rename_package_id_packagedatemodel_package'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packageplanmodel',
            old_name='package_id',
            new_name='package',
        ),
    ]
