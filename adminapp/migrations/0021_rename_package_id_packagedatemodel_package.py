# Generated by Django 5.0.2 on 2024-03-22 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_rename_nation_id_packagesmodel_nation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packagedatemodel',
            old_name='package_id',
            new_name='package',
        ),
    ]
