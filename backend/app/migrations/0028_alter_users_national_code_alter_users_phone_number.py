# Generated by Django 4.2 on 2023-06-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='national_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]