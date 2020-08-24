from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('orderItems', 'complete')

    def orderItems(self, obj):
        return obj.orderitem_set.all()


# Register your models here.
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
