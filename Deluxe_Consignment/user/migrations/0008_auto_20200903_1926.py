# Generated by Django 3.1 on 2020-09-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_order_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='amount',
        ),
        migrations.AddField(
            model_name='coupon',
            name='discount_percentage',
            field=models.FloatField(default=5),
        ),
    ]