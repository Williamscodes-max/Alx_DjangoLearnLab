from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    ListView:
    - Allows anyone to view all books (read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView:
    - Allows anyone to view a single book by ID
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    CreateView:
    - Allows only authenticated users to create a book
    - Uses serializer validation automatically
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView:
    - Allows only authenticated users to update a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView:
    - Allows only authenticated users to delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
