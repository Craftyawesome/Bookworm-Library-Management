from django.contrib import admin
from .models import User, Book   #classes that are in models.py

# Register your models here.
admin.site.register(User)
admin.site.register(Book)

class UserAdmin(admin.ModelAdmin):
    list_display =  ['id', 'name', 'phone_number', 'is_admin']

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_name', 'isbn', 'rent_flag', 'genre']