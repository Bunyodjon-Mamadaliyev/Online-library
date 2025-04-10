from django.urls import path
from .views import BookListCreateView, BookDetailView, SimilarBooksView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/similar/', SimilarBooksView.as_view(), name='book-similar'),
]
