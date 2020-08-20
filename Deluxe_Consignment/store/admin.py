from django.contrib import admin
from .models import *

admin.site.site_header = "Deluxe Consignment Shop Admin Dashboard"

# Register your models here.

admin.site.register(Shoe)
admin.site.register(Bag)
admin.site.register(Accessory)
admin.site.register(SLGS)
admin.site.register(ProductImage)
