# create.md

from bookshelf.models import Book

# Creating a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected output: <Book: Book object (1)> showing the created instance's ID.


# retrieve.md

# Retrieve the book we just created
retrieved_book = Book.objects.get(id=book.id)
retrieved_book  # Expected output: <Book: Book object (1)> displaying all attributes.


# update.md

# Update the title of the book
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book  # Expected output: <Book: Book object (1)> with updated title "Nineteen Eighty-Four".


# delete.md

# Delete the book
retrieved_book.delete()

# Confirm deletion
Book.objects.all()  # Expected output: <QuerySet []> indicating the book was successfully deleted.
