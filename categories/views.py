from rest_framework import generics
from .models import Category
from .serializers import CategorySerializerV1, CategorySerializerV2


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.version == "1":
            return CategorySerializerV1
        return CategorySerializerV2


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.version == "1":
            return CategorySerializerV1
        return CategorySerializerV2
