from rest_framework import serializers
from authors.serializers import AuthorSerializerV1
from categories.serializers import CategorySerializerV1
from .models import Book
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class BookSerializerV1(serializers.ModelSerializer):
    authors = AuthorSerializerV1(many=True)
    categories = CategorySerializerV1(many=True)

    class Meta:
        model = Book
        fields = (
            'id', 'title', 'description', 'authors', 'categories',
            'isbn', 'published_date', 'publisher', 'page_count',
            'language', 'cover_image', 'slug'
        )
        read_only_fields = ['created_at', 'updated_at']



class BookSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id',
                  'title_uz',
                  'title_ru',
                  'title_en',
                  'description_uz',
                  'description_ru',
                  'description_en',
                  'authors', 'categories',
                  'isbn', 'published_date',
                  'publisher_uz',
                  'publisher_ru',
                  'publisher_en',
                  'page_count',
                  'language_uz',
                  'language_ru',
                  'language_en',
                  'cover_image', 'slug', 'created_at', 'updated_at')
        read_only_fields = ['created_at', 'updated_at']




