from rest_framework import serializers
from .models import BookAvailability

class BookAvailabilitySerializerV1(serializers.ModelSerializer):
    class Meta:
        model = BookAvailability
        fields = ('id', 'book', 'status', 'quantity', 'available_from')

class BookAvailabilitySerializerV2(serializers.ModelSerializer):
    class Meta:
        model = BookAvailability
        fields = ('id',
                  'book_en',
                  'book_uz',
                  'book_ru',
                  'status', 'quantity', 'available_from')
        read_only_fields = ['available_from']
