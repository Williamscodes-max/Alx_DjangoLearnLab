from rest_framework import serializers
from .models import Author, Book
from datetime import date

# =========================
# Book Serializer
# =========================
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    Serializes all fields of Book and validates publication_year to prevent future dates.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# =========================
# Author Serializer
# =========================
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    
    Includes:
    - name: Author's name
    - books: Nested BookSerializer for all books written by this author
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
