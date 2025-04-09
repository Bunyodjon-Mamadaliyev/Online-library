from rest_framework import serializers
from .models import Author

class AuthorSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'bio')

class AuthorSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'bio', 'birth_date', 'death_date', 'slug', 'created_at', 'updated_at')
