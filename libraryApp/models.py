from django.db import models

# Create your models here.

# Book Model for datbase
class Book(models.Model):

    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery','Mystery'),
        ('Fantasy','Fantasy'),
        ('Thriller','Thriller'),
        ('Romance','Romance'),

    ]

    author_name     = models.CharField(max_length=255)
    title           = models.CharField(max_length=255)
    rent_flag       = models.BooleanField(default=True)
    isbn            = models.CharField(max_length=15)
    genre           = models.CharField(max_length=20, default='Fiction', choices=GENRE_CHOICES)

    def __str__(self):
        return self.title