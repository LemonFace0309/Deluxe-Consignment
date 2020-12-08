from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    list_filter = ('date_created',)

    class Meta:
        model = Blog

# Register your models here.
admin.site.register(Blog, BlogAdmin)