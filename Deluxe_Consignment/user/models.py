from django.db import models
from django.contrib.auth.models import User
from store.models import Product

COUNTRY_OPTIONS = (
    ('Canada', 'Canada'),
    ('USA', 'USA'),
    ('Mexico', 'Mexico'),
)

PROVINCE_OPTIONS = (
    ('Ontario', 'Ontario'),
    ('British Columbia', 'British Columbia'),
    ('Quebec', 'Quebec'),
    ('Alberta', 'Alberta'),
    ('Manitoba', 'Manitoba'),
    ('New Brunswick', 'New Brunswick'),
    ('Newfoundland and Labrador', 'Newfoundland and Labrador'),
    ('Northwest Territories', 'Northwest Territories'),
    ('Nova Scotia', 'Nova Scotia'),
    ('Nunavut', 'Nunavut'),
    ('Prince Edward Island', 'Prince Edward Island'),
    ('Saskatchewan', 'Saskatchewan'),
    ('Yukon', 'Yukon'),
)

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
<<<<<<< HEAD
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)
=======
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
>>>>>>> 22df31a110fc505e92d538a03e78cb58a0656575

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    shipping = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{str(self.id)} created by {self.customer.name}"

    @property
    def get_cart_total(self):
        items = self.orderitem_set.all()
        return sum([item.get_total for item in items])

    @property
    def get_cart_quantity(self):
        items = self.orderitem_set.all()
        return sum([item.quantity for item in items])


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    @property
    def get_total(self):
        return self.quantity * self.product.discount_price


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, choices=PROVINCE_OPTIONS, null=True)
    country = models.CharField(max_length=200, choices=COUNTRY_OPTIONS, null=True)
    postal_code = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
