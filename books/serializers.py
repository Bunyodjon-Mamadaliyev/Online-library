from rest_framework import serializers
from authors.serializers import AuthorSerializerV1
from categories.serializers import CategorySerializerV1
from .models import Book

class BookSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'authors', 'categories', 'isbn',)

class BookSerializerV2(serializers.ModelSerializer):
    authors = AuthorSerializerV1(many=True, read_only=True)
    categories = CategorySerializerV1(many=True, read_only=True)
    class Meta:
        model = Book
        fields = (
            'id',
            'title_uz', 'title_ru', 'title_en',
            'description_uz', 'description_ru', 'description_en',
            'authors', 'categories',
            'isbn', 'published_date',
            'publisher_uz', 'publisher_ru', 'publisher_en',
            'page_count',
            'language_uz', 'language_ru', 'language_en',
            'cover_image', 'slug',
            'created_at', 'updated_at'
        )
        read_only_fields = ['created_at', 'updated_at']
