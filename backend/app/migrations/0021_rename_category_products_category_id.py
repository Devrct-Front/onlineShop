# Generated by Django 4.2 on 2023-06-16 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_rename_category_id_products_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='category_id',
        ),
    ]
