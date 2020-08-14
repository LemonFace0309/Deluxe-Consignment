from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


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


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    shipping = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        items = self.orderitem_set.all()
        return sum([item.get_total for item in items])

    @property
    def get_cart_items(self):
        items = self.orderitem_set.all()
        return sum([item.quantity for item in items])


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        return self.quantity * self.product.price


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address






