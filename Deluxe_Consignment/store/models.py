from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.shortcuts import reverse
import datetime

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
    featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now=True)
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
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    @property
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })

    @property
    def is_new(self):
        DATE_FORMAT = "%Y-%m-%d"
        today = datetime.date.today()
        date_created = self.date_created.strftime(DATE_FORMAT)
        date_created = datetime.date(int(date_created[0:4]), int(date_created[5:7]), int(date_created[-2:]))
        if date_created + datetime.timedelta(days=7) > today:
            return True
        return False

    @property
    def get_brand(self):
        return self.get_brand_display()

    @property
    def is_shoe(self):
        return hasattr(self, "shoe")

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
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









