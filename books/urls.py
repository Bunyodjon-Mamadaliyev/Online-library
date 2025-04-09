from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books_list_create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='books-detail'),
    path('books/<slug:slug>/', views.BookDetailView.as_view(), name='books-detail-slug'),
]
