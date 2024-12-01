from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Retrieve, update, or delete a book by its ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Update a book by its ID
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book by its ID
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]