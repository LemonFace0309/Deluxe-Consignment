from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.shortcuts import reverse

BRAND_CHOICES = [
    ('Bal', 'Balenciaga'),
    ('Bur', 'Burberry'),
    ('Cel', 'Celine'),
    ('Cha', 'Chanel'),
    ('Dio', 'Christian Dior'),
    ('Loub', 'Christian Louboutins'),
    ('Fer', 'Ferragamo'),
    ('Giv', 'Givenchy'),
    ('Guc', 'Gucci'),
    ('Her', 'Hermes'),
    ('Choo', 'Jimmy Choo'),
    ('Vui', 'Louis Vuitton'),
    ('Pra', 'Prada'),
    ('Laur', 'Saint Laurent'),
    ('Gar', 'Valentino Garavani'),
    ('Oth', 'Others'),
]


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=4, choices=BRAND_CHOICES, null=True)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    discount_price = models.DecimalField(max_digits=99, decimal_places=2, blank=True, null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    slug = models.SlugField(max_length=200)
    # photos = ArrayField(ArrayField(models.ImageField(null=True, blank=True)))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={
            'slug': self.slug
        })

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)


class Shoe(Product, models.Model):
    size = models.IntegerField(default=10)


class Bag(Product, models.Model):
    pass


class Accessory(Product, models.Model):
    pass


class SLGS(Product, models.Model):
    pass









