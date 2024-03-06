from django.urls import path 
from .views import home, book_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('book_list/', book_list, name='book_list'),
    path("logout/", auth_views.LogoutView.as_view()),
]