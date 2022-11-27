# Generated by Django 4.1.2 on 2022-10-22 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(default=None, max_length=25)),
                ('Category', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2022, 10, 22, 19, 53, 25, 942468))),
                ('Price', models.CharField(blank=True, max_length=12, null=True)),
                ('Quantity', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user_data',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 22, 19, 53, 25, 942468)),
        ),
    ]
