from django.db import models
from django.utils import timezone


# Create your models here.

# Book Model for datbase
class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Romance', 'Romance'),

    ]

    author_name     = models.CharField(max_length=255)
    title           = models.CharField(max_length=255)
    rent_flag       = models.BooleanField(default=True)
    isbn            = models.CharField(max_length=15)
    genre           = models.CharField(max_length=20, default='Fiction', choices=GENRE_CHOICES)
    

    def __str__(self):
        return self.title


class Book_Request(models.Model):
    username = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    book_title = models.CharField(max_length=70)
    book_author = models.CharField(max_length=70)

class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
