from rest_framework import generics
from .serializers import BookSerializerV1, BookSerializerV2
from .models import Book


class BookListView(generics.ListAPIView):
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
