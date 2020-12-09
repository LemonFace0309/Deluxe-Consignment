from django.db.models.signals import post_save
from .models import *
from django.contrib.auth.models import User


def create_customer(sender, instance, created, **kwargs):

    if created:
        Customer.objects.create(user=instance, name=instance.first_name + ' ' + instance.last_name, email=instance.email)
        print('Customer Profile Created')

post_save.connect(create_customer, sender=User)


def update_customer(sender, instance, created, **kwargs):

    if created == False:
        instance.customer.email = instance.email
        instance.customer.name = instance.first_name + ' ' + instance.last_name
        instance.customer.save()
        print('Customer Profile Updated')

post_save.connect(update_customer, sender=User)







