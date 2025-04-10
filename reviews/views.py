from rest_framework import generics
from rest_framework.exceptions import NotFound
from django.db.models import Avg
from .models import Review
from books.serializers import BookSerializerV1, BookSerializerV2
from .serializers import ReviewSerializerV1, ReviewSerializerV2
from books.models import Book


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializerV2

    def get_queryset(self):
        book_id = self.kwargs.get("id")
        return Review.objects.filter(book_id=book_id)

    def get_serializer_class(self):
        if self.request.version == "1":
            return ReviewSerializerV1
        return ReviewSerializerV2

    def perform_create(self, serializer):
        book_id = self.kwargs.get("id")
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound(detail="Book not found.")
        serializer.save(book=book)


class TopRatedBooksView(generics.ListAPIView):
    serializer_class = BookSerializerV1

    def get_queryset(self):
        return Book.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:10]

    def get_serializer_class(self):
        if self.request.version == "1":
            return BookSerializerV1
        return BookSerializerV2
