from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints
    """

    def setUp(self):
        """
        Runs before every test.
        Creates a user and authenticates requests.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Authenticate all requests
        self.client.force_authenticate(user=self.user)

        self.author = Author.objects.create(name="Test Author")

        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        self.books_url = "/api/books/"

    def test_get_books_list(self):
        """
        Test retrieving list of books
        """
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        """
        Test creating a new book
        """
        data = {
            "title": "New Book",
            "publication_year": 2019,
            "author": self.author.id
        }

        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_single_book(self):
        """
        Test retrieving a single book
        """
        response = self.client.get(f"{self.books_url}{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        """
        Test updating a book
        """
        data = {
            "title": "Updated Title",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.put(f"{self.books_url}{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """
        Test deleting a book
        """
        response = self.client.delete(f"{self.books_url}{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)


class BookFilterSearchOrderTestCase(APITestCase):
    """
    Tests for filtering, searching, and ordering Book endpoints
    """

    def setUp(self):
        from django.contrib.auth.models import User
        from api.models import Author, Book

        self.user = User.objects.create_user(
            username="filteruser",
            password="filterpass123"
        )
        self.client.force_authenticate(user=self.user)

        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        Book.objects.create(
            title="Django Basics",
            publication_year=2018,
            author=self.author1
        )
        Book.objects.create(
            title="Advanced Django",
            publication_year=2022,
            author=self.author2
        )

        self.url = "/api/books/"

    def test_filter_books_by_author(self):
        """
        Test filtering books by author ID
        """
        response = self.client.get(self.url, {"author": self.author1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Basics")

    def test_search_books_by_title(self):
        """
        Test searching books by title
        """
        response = self.client.get(self.url, {"search": "Advanced"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Advanced Django")

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year
        """
        response = self.client.get(self.url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2018)

