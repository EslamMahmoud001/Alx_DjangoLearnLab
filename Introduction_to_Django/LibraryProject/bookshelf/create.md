# create.md

```python
from app1.models import Book

# Creating a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected output: <Book: Book object (1)> showing the created instance's ID.