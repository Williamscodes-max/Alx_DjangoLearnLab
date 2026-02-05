from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
        # Login the user for authenticated requests
        self.client.login(username='testuser', password='testpass123')

        # Create test author and book
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)

        # Define endpoint URLs
        self.books_url = '/api/books/'                 # list/create
        self.book_url = f'/api/books/{self.book.id}/'  # retrieve/update/delete

    # ✅ Test listing books
    def test_list_books(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ✅ Test creating a book
    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # ✅ Test retrieving a book
    def test_retrieve_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    # ✅ Test updating a book
    def test_update_book(self):
        data = {'title': 'Updated Book'}
        response = self.client.patch(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    # ✅ Test deleting a book
    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())


class BookFilterSearchOrderTestCase(APITestCase):
    def setUp(self):
        # Create test user and login
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        # Create books
        self.book1 = Book.objects.create(title='Alpha Book', publication_year=2019, author=self.author1)
        self.book2 = Book.objects.create(title='Beta Book', publication_year=2020, author=self.author2)

        # Endpoint URL
        self.books_url = '/api/books/'

    # ✅ Filter books by author
    def test_filter_books_by_author(self):
        response = self.client.get(self.books_url, {'author': self.author1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Alpha Book')

    # ✅ Search books by title
    def test_search_books_by_title(self):
        response = self.client.get(self.books_url, {'search': 'Beta'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Beta Book')

    # ✅ Order books by publication year
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.books_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Alpha Book')
