from django.contrib import admin
from .models import *

admin.site.site_header = "Deluxe Consignment Shop Admin Dashboard"


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    readonly_fields = ('date_created',)
    list_filter = ('date_created',)

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Shoe, ProductAdmin)
admin.site.register(Bag, ProductAdmin)
admin.site.register(Accessory, ProductAdmin)
admin.site.register(SLG, ProductAdmin)