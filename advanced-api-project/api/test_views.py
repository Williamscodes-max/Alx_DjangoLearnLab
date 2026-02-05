from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
from .models import Book, Author


# -----------------------------
# API CRUD Tests for Book model
# -----------------------------
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        
        # Client with token authentication
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create test author and book
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(title="Test Book", publication_year=2023, author=self.author)

        # ✅ Define URLs for your endpoints
        # Assuming you registered your viewset as 'books' in urls.py
        self.books_url = '/api/books/'              # list/create endpoint
        self.book_url = f'/api/books/{self.book.id}/'  # retrieve/update/delete endpoint


    def test_list_books(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        data = {
            'title': 'Harry Potter and the Chamber of Secrets',
            'publication_year': 1998,
            'author': self.author.id
        }
        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {'title': 'Harry Potter Updated'}
        response = self.client.patch(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Harry Potter Updated')

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

# -----------------------------------------------
# Filtering, Searching, and Ordering API Tests
# -----------------------------------------------
class BookFilterSearchOrderTestCase(APITestCase):

    def setUp(self):
        # Test user setup
        self.user = User.objects.create_user(username='testuser2', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Authors and books for testing
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George R.R. Martin')

        self.book1 = Book.objects.create(title='Harry Potter 1', publication_year=1997, author=self.author1)
        self.book2 = Book.objects.create(title='Harry Potter 2', publication_year=1998, author=self.author1)
        self.book3 = Book.objects.create(title='Game of Thrones', publication_year=1996, author=self.author2)

        self.books_url = '/api/books/'

    def test_filter_books_by_author(self):
        response = self.client.get(self.books_url, {'author': self.author2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Game of Thrones')

    def test_search_books_by_title(self):
        response = self.client.get(self.books_url, {'search': 'Harry Potter 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 1')

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.books_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
