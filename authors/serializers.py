from rest_framework import serializers
from .models import Author

class AuthorSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'slug']

class AuthorSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id',
                  'first_name_en',
                  'first_name_uz',
                  'first_name_ru',
                  'last_name_en',
                  'last_name_uz',
                  'last_name_ru',
                  'slug']
