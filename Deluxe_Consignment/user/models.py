from django.db import models
from django.shortcuts import reverse
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
    ('California', 'California')
)

DELIVERY_OPTIONS = (
    ('Shipping', 'Shipping'),
    ('Pick-up', 'Pick-up')
)


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    delivery = models.CharField(max_length=100, choices=DELIVERY_OPTIONS, default='Pick-up',
                                null=True, blank=True)
    shipping_cost = models.FloatField(null=True, blank=True)
    layaway = models.BooleanField(default=False)
    tax = models.FloatField(null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{str(self.id)} created by {str(self.customer)}"

    @property
    def get_subtotal(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        total = float(total)
        return total

    @property
    def get_cart_total(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        total = float(total)
        if self.coupon:
            total *= (1 - (self.coupon.discount_percentage/100))
        if self.tax:
            total *= 1 + (self.tax / 100)
        if self.shipping_cost:
            total += self.shipping_cost
        return total

    @property
    def get_cart_ontario_tax_total(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        total = float(total)
        if self.coupon:
            total *= (1 - (self.coupon.discount_percentage/100))
        total *= 1.13
        if self.shipping_cost:
            total += self.shipping_cost
        return total

    @property
    def get_cart_quantity(self):
        items = self.orderitem_set.all()
        return sum([item.quantity for item in items])

    @property
    def get_discount_total(self):
        if self.coupon:
            items = self.orderitem_set.all()
            total = float(sum([item.get_total for item in items]))
            total = total - total * (1 - (self.coupon.discount_percentage / 100))
            return total
        return 0

    @property
    def get_tax_total(self):
        if self.tax:
            items = self.orderitem_set.all()
            total = float(sum([item.get_total for item in items])) - self.get_discount_total
            total = total * (1 + (self.tax / 100)) - total
            return total
        return 0

    @property
    def get_ontario_tax_total(self):
        items = self.orderitem_set.all()
        total = float(sum([item.get_total for item in items])) - self.get_discount_total
        total = total * 1.13 - total
        return total

    @property
    def get_shipping_address(self):
        return self.shippingaddress_set.first()


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
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.address

    def get_remove_address_url(self):
        return reverse("user:remove-address", kwargs={
            'id': self.id
        })

    def get_edit_address_url(self):
        return reverse("user:edit-address", kwargs={
            'id': self.id
        })


class Coupon(models.Model):
    code = models.CharField(max_length=25)
    discount_percentage = models.FloatField(default=5)

    def __str__(self):
        return self.code


class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    message = models.TextField(max_length=5000)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}\'s Message'


# Note: subscriber is not attached to a user until user account is created
class EmailSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
