from django.shortcuts import render
from .models import Book
# Create your views here.

# HomeScreenView
def home(request):
    return render(request, 'home.html')


def book_list(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    if query:
        # Perform a case-insensitive search on title and author fields
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author_name__icontains=query)
    else:
        # If no query, return all books
        books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books, 'query': query})

