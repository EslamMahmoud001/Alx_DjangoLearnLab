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
