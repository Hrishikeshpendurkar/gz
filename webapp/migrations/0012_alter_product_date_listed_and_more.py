# Generated by Django 4.1.2 on 2022-10-23 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_product_brand_product_chipset_product_colour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_listed',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 15, 6, 46, 545807)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 15, 6, 46, 544807)),
        ),
    ]
