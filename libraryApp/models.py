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
    price           = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)

    def __str__(self):
        return self.title


class Book_Request(models.Model):
    username = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    book_title = models.CharField(max_length=70)
    book_author = models.CharField(max_length=70)

#class Rental(model.Modles):
#    book        = models.ForeignKey(Book, on_delete=models.CASCADE)
#    rented_by   = models.CharField(max_length=100)
#    rented_on   = models.DateTimeField(default=timezone.now)
#    due_date    = models.DateTimeField()
#    returned    = models.BooleanField(default=False)

#    def __str__(self):
#        return f"{self.book} rented by {self.rented_by}"


class NuBook(models.Model):
    class Condition(models.IntegerChoices):
        NEW = 0
        FINE = 1
        VERYGOOD = 2
        GOOD = 3
        FAIR = 4
        POOR = 5
        RETIRED = 6

    # django automatically adds an ID entry
    ISBN = models.CharField(max_length=13)  # ISBN-13
    condition = models.IntegerField(choices=Condition)


class BookData(models.Model):
    class Genres(models.IntegerChoices):
        NONFICTION = 0
        FICTION = 1
        POETRY = 2
        DRAMA = 3
        PROSE = 4
        MYSTERY = 5
        ROMANCE = 6
        EROTIC = 7
        FANTASY = 8
        SCIFI = 9
        ACTION = 10
        HORROR = 11
        COMEDY = 12
        HISTORY = 13

    ISBN = models.CharField(max_length=13, primary_key=True)
    author_names = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    dewey_decmial = models.IntegerField()
    display_genre = models.IntegerField(choices=Genres)


class Transactions(models.Model):
    # django generates IDs for us here
    book_id = models.ForeignKey("NuBook", on_delete=models.CASCADE)
    # userid - need to ask about how the users db works
    outDate = models.DateField()
    inDate = models.DateField()