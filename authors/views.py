from rest_framework import generics
from .serializers import AuthorSerializerV1, AuthorSerializerV2
from .models import Author


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.version == "1":
            return AuthorSerializerV1
        return AuthorSerializerV2

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.version == "1":
            return AuthorSerializerV1
        return AuthorSerializerV2
