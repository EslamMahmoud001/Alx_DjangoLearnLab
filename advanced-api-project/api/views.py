from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(generics.ListCreateAPIView):
    """
    View to list all books and create a new book.
    - GET /books/: Returns a list of all books.
    - POST /books/: Creates a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users
    
    def perform_create(self, serializer):
        """
        Custom logic to handle the creation of a book instance.
        """
        # Custom behavior (e.g., add extra fields or log actions)
        serializer.save()  # Save the book

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific book.
    - GET /books/<id>/: Retrieve a book by its ID.
    - PUT /books/<id>/: Update a specific book (authenticated users only).
    - DELETE /books/<id>/: Delete a specific book (authenticated users only).
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users
    
