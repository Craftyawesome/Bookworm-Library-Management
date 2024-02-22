from django.urls import path 
from .views import home, book_list

urlpatterns = [
    path('', home, name='home'),
    path('book_list/', book_list, name='book_list'),

]