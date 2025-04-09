from rest_framework import generics
from .serializers import ReviewSerializerV1, ReviewSerializerV2
from .models import Review


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.version == "1":
            return ReviewSerializerV1
        return ReviewSerializerV2

