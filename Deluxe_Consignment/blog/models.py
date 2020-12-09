from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100, default="Jenny Liu", null=True, blank=True)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnails')
    content = models.TextField(max_length=50000, default="Content")
    slug = models.SlugField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url
