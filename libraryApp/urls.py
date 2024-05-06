from django.urls import path 

from .views import home, book_list, genre_view, getBook_Request, book_detail, add_to_cart, request_book, book_request, BookCheckoutView, delete_document

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('book_list/', book_list, name='book_list'),
    path("logout/", auth_views.LogoutView.as_view()),
    path('genre_view/',genre_view, name='genre_view'),
    path('book_detail/',book_detail, name='book_detail'),
    path('getBook_Request',views.getBook_Request, name='getBook_Request'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('book_checkout_list/', BookCheckoutView.as_view(), name='book_checkout_list'),
    path('<int:pk>/delete/', delete_document, name='book_checkout_delete'),
    path('request_book/', request_book, name='request_book'),
    path('book_request/', book_request, name='book_request'),


    

    
]