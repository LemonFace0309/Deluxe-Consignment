# Generated by Django 3.1 on 2020-09-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_merge_20200829_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
