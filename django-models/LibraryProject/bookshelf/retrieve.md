# retrieve.md

# Retrieve the book we just created (assuming it has the ID of 1)
retrieved_book = Book.objects.get(id=1)
retrieved_book

# Expected output:
# <Book: Book object (1)>  # This will display the book's representation, which includes the title, author, and published date.
# To see all attributes, you can also do:
# retrieved_book.title  # Expected output: "1984"
# retrieved_book.author  # Expected output: "George Orwell"
# retrieved_book.published_date  # Expected output: datetime.date(1949, 1, 1)