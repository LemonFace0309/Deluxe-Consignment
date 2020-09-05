from django.contrib import admin
from .models import *


class OrderItemAdmin(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]

    class Meta:
        model = Order


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Customer)
admin.site.register(ShippingAddress)
