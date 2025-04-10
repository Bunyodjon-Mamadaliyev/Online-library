from rest_framework import generics
from rest_framework.exceptions import NotFound
from .serializers import BookSerializerV1, BookSerializerV2
from .models import Book

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.version == "1":
            return BookSerializerV1
        return BookSerializerV2

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.version == "1":
            return BookSerializerV1
        return BookSerializerV2

class SimilarBooksView(generics.ListAPIView):
    serializer_class = BookSerializerV1

    def get_queryset(self):
        book_id = self.kwargs.get('id')
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound(detail="Book not found.")
        author = book.author
        return Book.objects.filter(author=author).exclude(id=book_id)



