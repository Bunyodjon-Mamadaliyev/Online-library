from django.urls import path
from .views import ReviewListCreateView, TopRatedBooksView

urlpatterns = [
    path('books/<int:id>/reviews/', ReviewListCreateView.as_view(), name='book-reviews'),
    path('books/top-rated/', TopRatedBooksView.as_view(), name='top-rated-books'),

]
