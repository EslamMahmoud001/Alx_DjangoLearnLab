import django
from django.conf import settings
from relationship_app.models import Author, Book, Library, Librarian

# Initialize Django settings
django.setup()

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"Author {author_name} not found.")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"Library {library_name} not found.")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"The librarian for {library_name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"Library {library_name} not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned for {library_name}.")

if __name__ == "__main__":
    # Example queries
    author_name = "J.K. Rowling"  # Change this to an actual author in your database
    library_name = "City Library"  # Change this to an actual library in your database

    get_books_by_author(author_name)
    list_books_in_library(library_name)
    get_librarian_for_library(library_name)