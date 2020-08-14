from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(default="a")
    price = models.IntegerField();

class Shoe(Product, models.Model):
    size = models.IntegerField(default=10)

class Bag(Product, models.Model):
    pass