# Generated by Django 3.1 on 2020-09-13 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200911_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='province',
            field=models.CharField(choices=[('Ontario', 'Ontario'), ('British Columbia', 'British Columbia'), ('Quebec', 'Quebec'), ('Alberta', 'Alberta'), ('Manitoba', 'Manitoba'), ('New Brunswick', 'New Brunswick'), ('Newfoundland and Labrador', 'Newfoundland and Labrador'), ('Northwest Territories', 'Northwest Territories'), ('Nova Scotia', 'Nova Scotia'), ('Nunavut', 'Nunavut'), ('Prince Edward Island', 'Prince Edward Island'), ('Saskatchewan', 'Saskatchewan'), ('Yukon', 'Yukon'), ('California', 'California')], max_length=200, null=True),
        ),
    ]