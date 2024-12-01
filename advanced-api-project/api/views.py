# api/views.py
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """
    View to list all books.
    - GET /books/: Returns a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only access to unauthenticated users
    
    # Enable filtering, searching, and ordering
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    
    # Filtering options: Allow filtering by title, author, and publication_year
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Search options: Enable searching by title and author
    search_fields = ['title', 'author__name']
    
    # Ordering options: Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering is by title

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    - POST /books/: Creates a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication to create a book

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a specific book.
    - GET /books/<id>/: Retrieve a book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only access to unauthenticated users

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    View to update a specific book.
    - PUT /books/<id>/: Update a book by its ID (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication to update a book

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a specific book.
    - DELETE /books/<id>/: Delete a book by its ID (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication to delete a book
