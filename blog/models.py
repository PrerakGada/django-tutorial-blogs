from django.db import models
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title