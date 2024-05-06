from django.urls import path 

from .views import home, book_list, requested_books, getBook_Request, book_detail, add_to_cart, request_book, BookCheckoutView, delete_document

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('book_list/', book_list, name='book_list'),
    path("logout/", auth_views.LogoutView.as_view()),
    path('requested_books/',requested_books, name='requested_books'),
    path('book_detail/',book_detail, name='book_detail'),
    path('getBook_Request',views.getBook_Request, name='getBook_Request'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('book_checkout_list/', BookCheckoutView.as_view(), name='book_checkout_list'),
    path('<int:pk>/delete/', delete_document, name='book_checkout_delete'),
    path('request_book/', request_book.as_view(), name='request_book'),


    

    
]