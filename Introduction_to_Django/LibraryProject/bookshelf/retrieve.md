# retrieve.md

```python
# Retrieve the book we just created
retrieved_book = Book.objects.get(id=book.id)
retrieved_book  # Expected output: <Book: Book object (1)> displaying all attributes.
