from django.shortcuts import render
from .models import Book
# Create your views here.

# HomeScreenView
def home(request):
    genres = Book.GENRE_CHOICES

    grouped_books = {}
    for genre, _ in genres:
        books = Book.objects.filter(genre=genre)
        grouped_books[genre] = books

    context = {
        'grouped_books': grouped_books,
    }

    return render(request, 'home.html', context)

def book_list(request):
    # Get the search query from the URL parameter 'q'
    query = request.GET.get('q', '')

    if query:
        # Perform a case-insensitive search on title and author fields
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author_name__icontains=query)
    else:
        # If no query, return all books
        books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books, 'query': query})

