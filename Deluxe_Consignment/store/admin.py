from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

admin.site.register(Shoe)
admin.site.register(Bag)
admin.site.register(Accessory)
admin.site.register(SLGS)
