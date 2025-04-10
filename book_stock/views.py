from rest_framework import generics
from .models import BookAvailability
from .serializers import BookAvailabilitySerializerV1, BookAvailabilitySerializerV2

class BookAvailabilityListCreateView(generics.ListCreateAPIView):
    queryset = BookAvailability.objects.all()

    def get_serializer_class(self):
        if self.request.version == "1":
            return BookAvailabilitySerializerV1
        return BookAvailabilitySerializerV2

class BookAvailabilityDetailView(generics.RetrieveAPIView):
    queryset = BookAvailability.objects.all()
    lookup_field = "book_id"

    def get_serializer_class(self):
        if self.request.version == "1":
            return BookAvailabilitySerializerV1
        return BookAvailabilitySerializerV2
