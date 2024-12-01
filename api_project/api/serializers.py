from rest_framework import serializers
from .models import Book  # Assuming you have a Book model in the api app

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model