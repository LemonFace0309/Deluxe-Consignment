# Generated by Django 3.1 on 2020-12-06 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(default='Content', max_length=5000),
        ),
        migrations.AddField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Title', max_length=100),
        ),
    ]
