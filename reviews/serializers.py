from rest_framework import serializers
from .models import Review

class ReviewSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'book', 'user_name', 'comment')


class ReviewSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'book', 'user_name', 'rating', 'comment', 'created_at')
        read_only_fields = ['created_at']


