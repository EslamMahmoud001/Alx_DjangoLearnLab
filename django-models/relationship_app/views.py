from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Create your views here.

def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html', "library", "from .models import Library"
    context_object_name = 'library'