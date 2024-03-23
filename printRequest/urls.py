from django.urls import path
from .views import HomePageView, CreatePostView, delete_document

urlpatterns = [
    path("", HomePageView.as_view(), name="print_list"),
    path("post/", CreatePostView.as_view(), name="print_request"),
    path('<int:pk>/delete/', delete_document, name='print_delete'),
]
