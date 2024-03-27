from django.urls import path 
from .views import home, book_list, genre_view, getBook_Request
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('book_list/', book_list, name='book_list'),
    path("logout/", auth_views.LogoutView.as_view()),
    path('genre_view/',genre_view, name='genre_view'),
    path('getBook_Request',views.getBook_Request, name='getBook_Request'),
]