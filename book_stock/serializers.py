from rest_framework import serializers
from .models import BookAvailability

class BookAvailabilitySerializerV1(serializers.ModelSerializer):
    class Meta:
        model = BookAvailability
        fields = ('id', 'book', 'status')

class BookAvailabilitySerializerV2(serializers.ModelSerializer):
    class Meta:
        model = BookAvailability
        fields = ('id', 'book', 'status', 'quantity', 'available_from')
        read_only_fields = ['available_from']


# class BookAvailabilitySerializerV2(serializers.ModelSerializer):
#     class Meta:
#         model = BookAvailability
#         fields = ('id',
#                   'book_uz',
#                   'book_ru',
#                   'book_en',
#                   'status_uz',
#                   'status_ru',
#                   'status_en',
#                   'quantity',
#                   'quantity',
#                   'quantity',
#                   'available_from'
#                   'available_from'
#                   'available_from'
#                   )
#
