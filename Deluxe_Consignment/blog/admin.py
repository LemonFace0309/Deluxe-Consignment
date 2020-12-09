from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    list_filter = ('date_created',)

    class Meta:
        model = Post

# Register your models here.
admin.site.register(Post, PostAdmin)