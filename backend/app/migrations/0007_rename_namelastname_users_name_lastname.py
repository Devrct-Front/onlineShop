# Generated by Django 4.2.1 on 2023-06-11 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_country_users_namelastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='namelastname',
            new_name='name_lastname',
        ),
    ]
