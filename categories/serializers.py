from rest_framework import serializers
from .models import Category

class CategorySerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',  'description', 'slug', 'created_at', 'updated_at')

class CategorySerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name_uz',
                  'name_ru',
                  'name_en',
                  'description_uz',
                  'description_ru',
                  'description_en',
                  'slug', 'created_at', 'updated_at')
        read_only_fields = ['created_at', 'updated_at']
