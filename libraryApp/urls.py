from django.urls import path 
from .views import home, book_list, genre_view, getBook_Request, book_detail, book_club
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('book_list/', book_list, name='book_list'),
    path('book_club/', book_club, name='book_club'),
    path("logout/", auth_views.LogoutView.as_view()),
    path('genre_view/',genre_view, name='genre_view'),
    path('book_detail/',book_detail, name='book_detail'),
    path('getBook_Request',views.getBook_Request, name='getBook_Request'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),


    

    
]