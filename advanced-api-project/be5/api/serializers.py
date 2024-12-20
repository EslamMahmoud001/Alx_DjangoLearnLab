from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model. Includes a custom validation to ensure the publication year
    is not in the future.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include the related books dynamically
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']