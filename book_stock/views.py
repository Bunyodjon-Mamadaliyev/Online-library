from rest_framework import generics
from .serializers import BookAvailabilitySerializerV1, BookAvailabilitySerializerV2
from .models import BookAvailability


class BookAvailabilityListCreateView(generics.ListCreateAPIView):
    queryset = BookAvailability.objects.all()

    def get_serializer_class(self):
        if self.request.version == "1":
            return BookAvailabilitySerializerV1
        return BookAvailabilitySerializerV2

class BookAvailabilityDetailView(generics.RetrieveAPIView):
    queryset = BookAvailability.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.version == "1":
            return BookAvailabilitySerializerV1
        return BookAvailabilitySerializerV2
