from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Book_Request, CartItem
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
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
    query = request.GET.get('q', '').strip()

    if query:
        # Perform a case-insensitive search on title and author fields
        books = Book.objects.filter(title__icontains=query) | \
                Book.objects.filter(author_name__icontains=query) | \
                Book.objects.filter(isbn__exact=query)
    else:
        # If no query, return all books
        books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books, 'query': query})

def genre_view(request):

        return render(request, 'genre_view.html')

def book_detail(request, book_id):
    # Retrieve the book object using its ID
    book = get_object_or_404(Book, id=book_id)
    
    # Define the fields you want to display
    book_details = {
        'Title': book.title,
        'Author': book.author_name,
        'ISBN': book.isbn,
        'Genre': book.genre,
        'Rentable': book.rent_flag,
    }
    
    # Render the book detail template with the book details
    return render(request, 'book_detail.html', {'book_details': book_details})

def getBook_Request(request):
    requests = Book_Request.objects.all()
            
    return JsonResponse({"requests":list(requests.values())})

def book_club(request):
    return render(request,'book_club.html')


def add_to_cart(request):
    if request.method == 'POST':
        book_isbn = request.POST.get('book_isbn')
        book = get_object_or_404(Book, isbn=book_isbn)

        cart, created = Cart.objects.get_or_create(user=request.user)
        # Create a new CartItem for the selected book and add it to the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

        return redirect('home') #redirct to home page after adding to cart
    return redirect ('book_list') # redirct to book list if not a post request

def request_book(request):
    return render(request,'request_book.html')

def book_request(request):
    return render(request,'book_request.html')