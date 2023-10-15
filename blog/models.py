from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)
