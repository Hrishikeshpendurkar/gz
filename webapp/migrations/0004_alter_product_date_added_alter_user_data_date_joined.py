# Generated by Django 4.1.2 on 2022-10-22 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_product_date_added_alter_user_data_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 22, 19, 57, 20, 24519)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 22, 19, 57, 20, 23518)),
        ),
    ]
