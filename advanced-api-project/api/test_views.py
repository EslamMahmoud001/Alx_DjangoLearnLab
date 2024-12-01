from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

class BookApiTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a sample author and books for testing
        author = Author.objects.create(name='George Orwell')
        Book.objects.create(title='1984', author=author, publication_year=1949)
        Book.objects.create(title='Animal Farm', author=author, publication_year=1945)

        # Create a test user
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_book(self):
        """Test creating a book works as expected."""
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Brave New World', 'author': 1, 'publication_year': 1932}
        response = self.client.post('/api/books/create/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=3).title, 'Brave New World')

    def test_create_book_unauthenticated(self):
        """Test creating a book fails without authentication."""
        data = {'title': 'Brave New World', 'author': 1, 'publication_year': 1932}
        response = self.client.post('/api/books/create/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_books(self):
        """Test retrieving a list of books with filtering, search, and ordering."""
        response = self.client.get('/api/books/', {'ordering': 'publication_year'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')  # Check if it's ordered by publication year

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get('/api/books/', {'title': '1984'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_update_book(self):
        """Test updating an existing book."""
        book = Book.objects.first()
        data = {'title': '1984 Revised', 'author': book.author.id, 'publication_year': 1950}
        self.client.login(username='testuser', password='testpassword')
        response = self.client.put(f'/api/books/{book.id}/update/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, '1984 Revised')
        self.assertEqual(book.publication_year, 1950)

    def test_update_book_unauthenticated(self):
        """Test that an unauthenticated user cannot update a book."""
        book = Book.objects.first()
        data = {'title': '1984 Revised', 'author': book.author.id, 'publication_year': 1950}
        response = self.client.put(f'/api/books/{book.id}/update/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book(self):
        """Test deleting a book."""
        book = Book.objects.first()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(f'/api/books/{book.id}/delete/', format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Test that an unauthenticated user cannot delete a book."""
        book = Book.objects.first()
        response = self.client.delete(f'/api/books/{book.id}/delete/', format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_check(self):
        """Test that only authenticated users can perform create, update, and delete actions."""
        response = self.client.post('/api/books/create/', {'title': 'New Book', 'author': 1, 'publication_year': 2024}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Unauthenticated user

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/api/books/create/', {'title': 'New Book', 'author': 1, 'publication_year': 2024}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Authenticated user