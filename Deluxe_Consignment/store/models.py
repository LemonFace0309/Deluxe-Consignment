from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.shortcuts import reverse
import datetime

BRAND_CHOICES = [
    ('Balenciaga', 'Balenciaga'),
    ('Burberry', 'Burberry'),
    ('Celine', 'Celine'),
    ('Chanel', 'Chanel'),
    ('Christian Dior', 'Christian Dior'),
    ('Christian Louboutins', 'Christian Louboutins'),
    ('Ferragamo', 'Ferragamo'),
    ('Givenchy', 'Givenchy'),
    ('Gucci', 'Gucci'),
    ('Hermes', 'Hermes'),
    ('Jimmy Choo', 'Jimmy Choo'),
    ('Louis Vuitton', 'Louis Vuitton'),
    ('Prada', 'Prada'),
    ('Saint Laurent', 'Saint Laurent'),
    ('Valentino Garavani', 'Valentino Garavani'),
    ('Others', 'Others'),
]


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES, null=True)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    discount_price = models.DecimalField(max_digits=99, decimal_places=2, blank=True, null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    slug = models.SlugField(max_length=200)

    # setting a discount price equal to price if not set by admin
    def save(self, *args, **kwargs):
        if not self.discount_price:
            self.discount_price = self.price
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product-detail", kwargs={
            'slug': self.slug
        })

    @property
    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart", kwargs={
            'slug': self.slug
        })

    @property
    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart", kwargs={
            'slug': self.slug
        })

    @property
    def get_subtract_from_cart_url(self):
        return reverse("shop:subtract-from-cart", kwargs={
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
    def is_bag(self):
        return hasattr(self, "bag")

    @property
    def is_accessory(self):
        return hasattr(self, "accessory")

    @property
    def is_slg(self):
        return hasattr(self, "slgs")

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url

    @property
    def get_savings(self):
        if self.discount_price:
            return self.price - self.discount_price
        return 0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product.name


class Shoe(Product, models.Model):
    size = models.IntegerField(default=10)


class Bag(Product, models.Model):
    pass


class Accessory(Product, models.Model):
    pass


class SLG(Product, models.Model):
    pass









