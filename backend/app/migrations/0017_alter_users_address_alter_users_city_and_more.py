# Generated by Django 4.2.1 on 2023-06-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_maneger_name_alter_maneger_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='name_lastname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='national_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
