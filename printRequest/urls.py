from django.urls import path
from .views import HomePageView, delete_document

urlpatterns = [
    path("", HomePageView.as_view(), name="print"),
    path('<int:pk>/delete/', delete_document, name='print_delete'),
]
