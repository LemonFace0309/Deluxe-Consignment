from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(default="a")
    price = models.IntegerField(default=1)
    thumbnail = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    description = models.TextField(max_length=2000, null=True, blank=True)


class Shoe(Product, models.Model):
    size = models.IntegerField(default=10)


class Bag(Product, models.Model):
    pass


class Accessory(Product, models.Model):
    pass


class SLGS(Product, models.Model):
    pass


