from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query the Book model
    serializer_class = BookSerializer  # Use the BookSerializer to format the data
    
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Queryset for retrieving, updating, and deleting books
    serializer_class = BookSerializer  # Serializer for formatting book data