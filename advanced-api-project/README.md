# 

# Book API Documentation

## Endpoints

### `GET /books/`
- Retrieves a list of all books.

### `GET /books/<id>/`
- Retrieves a specific book by ID.

### `POST /books/`
- Creates a new book (authentication required).

### `PUT /books/<id>/`
- Updates a specific book (authentication required).

### `DELETE /books/<id>/`
- Deletes a specific book (authentication required).

## Authentication

- Endpoints that modify data (POST, PUT, DELETE) require authentication.
- The `GET /books/` and `GET /books/<id>/` endpoints are accessible to all users, authenticated or not.

### Advanced Querying for Books

The API supports the following query options:

1. **Filtering**:
   - Filter by `title`: `/books/?title=<value>`
   - Filter by `author`: `/books/?author__name=<value>`
   - Filter by `publication_year`: `/books/?publication_year=<value>`

2. **Search**:
   - Search by `title` or `author`: `/books/?search=<value>`

3. **Ordering**:
   - Order by `title`: `/books/?ordering=title`
   - Order by `publication_year`: `/books/?ordering=publication_year`
   - Order in descending order: `/books/?ordering=-publication_year`
