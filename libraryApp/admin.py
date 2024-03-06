from django.contrib import admin
from .models import Book   #classes that are in models.py

# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_name', 'isbn', 'rent_flag', 'genre']