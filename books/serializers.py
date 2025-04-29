from rest_framework import serializers
from .models import Book
from authors.models import Author
from categories.models import Category


class AuthorSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'slug']


class CategorySerializer1(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class BookSerializerV1(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all()
    )
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'description', 'authors', 'categories',
            'isbn', 'published_date', 'publisher', 'page_count',
            'language', 'cover_image', 'slug'
        ]
        extra_kwargs = {
            'authors': {'required': False},
            'categories': {'required': False}
        }

    def get_cover_image(self, obj):
        request = self.context.get('request')
        if obj.cover_image and request:
            return request.build_absolute_uri(obj.cover_image.url)
        return None

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # authors ni nested qilib chiqaramiz
        rep['authors'] = AuthorSerializer1(instance.authors.all(), many=True).data

        # categories ni nested qilib chiqaramiz
        rep['categories'] = CategorySerializer1(instance.categories.all(), many=True).data

        return rep

    def create(self, validated_data):
        authors_data = validated_data.pop('authors', [])
        categories_data = validated_data.pop('categories', [])
        book = Book.objects.create(**validated_data)
        book.authors.set(authors_data)
        book.categories.set(categories_data)
        return book

class BookSerializerV2(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)


    class Meta:
        model = Book
        fields = [
            'id',
            'title_en',
            'title_uz',
            'title_ru',
            'description_en',
            'description_uz',
            'description_ru',
            'authors', 'categories', 'isbn',
            'published_date', 'publisher', 'page_count', 'language',
            'cover_image', 'slug'
        ]
