from django.contrib import admin

from readpro.models.book import Book
from readpro.models.category import Category
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)