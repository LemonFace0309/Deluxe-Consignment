from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, default="Title")
    content = models.TextField(max_length=5000, default="Content")
    date_created = models.DateTimeField(default=timezone.now)
    