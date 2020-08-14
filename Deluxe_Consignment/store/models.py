from django.db import models
# from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Product(models.Model):
    name = models.TextField(default="a")
    price = models.IntegerField(default=1)
    thumbnail = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    # photos = ArrayField(ArrayField(models.ImageField(null=True, blank=True)))

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Shoe(Product, models.Model):
    size = models.IntegerField(default=10)


class Bag(Product, models.Model):
    pass


class Accessory(Product, models.Model):
    pass


class SLGS(Product, models.Model):
    pass









