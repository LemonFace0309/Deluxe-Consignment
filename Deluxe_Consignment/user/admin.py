from django.contrib import admin
from .models import *


class OrderItemAdmin(admin.StackedInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    readonly_fields = ('date_created',)
    list_filter = ('date_created',)

    list_display = ('__str__', 'date_created', 'complete')

    class Meta:
        model = Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Coupon)
