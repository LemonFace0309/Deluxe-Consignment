# Generated by Django 3.1 on 2020-12-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_merge_20201208_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Not Ordered', 'Not Ordered'), ('In Progress', 'In Progress'), ('Shipped', 'Shipped'), ('Ready for Pickup', 'Ready for Pickup'), ('Complete', 'Complete')], default='Not Ordered', max_length=100),
        ),
    ]
