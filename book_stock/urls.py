from django.urls import path
from .views import BookAvailabilityListCreateView, BookAvailabilityDetailView

urlpatterns = [
    path('books/<int:book_id>/availability/', BookAvailabilityDetailView.as_view(), name='book-availability-detail'),
    path('availability/', BookAvailabilityListCreateView.as_view(), name='book-availability-list-create'),
]
