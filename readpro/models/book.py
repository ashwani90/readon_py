from django.db import models
from django.contrib.auth.models import User

from readpro.models.category import Category

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    content_file = models.FileField()
    analysis_file = models.FileField()
    uploaded_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'books'

    def __str__(self):
        return f'{self.name}'