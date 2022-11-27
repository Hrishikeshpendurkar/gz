# Generated by Django 4.1.2 on 2022-10-23 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_product_date_listed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/product_image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_listed',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 13, 8, 33, 689827)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 13, 8, 33, 688827)),
        ),
    ]
