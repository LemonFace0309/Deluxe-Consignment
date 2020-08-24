from django.contrib import admin
from .models import *

admin.site.site_header = "Deluxe Consignment Shop Admin Dashboard"


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)

    list_filter = ('date_created',)


# Register your models here.
admin.site.register(Shoe, ProductAdmin)
admin.site.register(Bag, ProductAdmin)
admin.site.register(Accessory, ProductAdmin)
admin.site.register(SLGS, ProductAdmin)
admin.site.register(ProductImage)
