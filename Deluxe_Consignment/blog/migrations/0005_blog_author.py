# Generated by Django 3.1 on 2020-12-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201208_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, default='Jenny Liu', max_length=100, null=True),
        ),
    ]
