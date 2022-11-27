# Generated by Django 4.1.2 on 2022-10-25 11:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_categories_product_image_alter_product_date_listed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default=None, max_length=25)),
                ('product_image', models.ImageField(blank=True, default=None, null=True, upload_to='static/images/uploads/product_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Categories3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default=None, max_length=25)),
                ('product_image', models.ImageField(blank=True, default=None, null=True, upload_to='static/images/uploads/product_image/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_listed',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 16, 53, 58, 229121)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 16, 53, 58, 213494)),
        ),
        migrations.AddField(
            model_name='product',
            name='category2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.categories2'),
        ),
        migrations.AddField(
            model_name='product',
            name='category3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.categories3'),
        ),
    ]