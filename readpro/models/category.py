from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'