from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query the Book model
    serializer_class = BookSerializer  # Use the BookSerializer to format the data