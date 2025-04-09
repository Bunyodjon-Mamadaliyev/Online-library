from rest_framework import generics
from .serializers import AuthorSerializerV1, AuthorSerializerV2
from .models import Author


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.version == "1":
            return AuthorSerializerV1
        return AuthorSerializerV2