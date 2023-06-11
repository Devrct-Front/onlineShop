# Generated by Django 4.2.1 on 2023-06-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_users_city_users_email_alter_users_name_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='users',
            name='national_code',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='name_lastname',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
