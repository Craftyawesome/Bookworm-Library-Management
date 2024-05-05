from django.contrib import admin

#classes that are in models.py
from .models import Book, Book_Request, CartItem 

# Register your models here.
admin.site.register(Book)
admin.site.register(Book_Request)
admin.site.register(CartItem)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_name', 'isbn', 'genre', 'rent_flag']

class Book_Request(admin.ModelAdmin):
    list_display = ['username', 'email','book_title','book_author']