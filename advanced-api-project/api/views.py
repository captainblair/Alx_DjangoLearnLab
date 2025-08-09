from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books (public access)
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Lists all books. Read-only for all users (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # public read


# Retrieve a single book (public access)
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Retrieves a specific book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # public read


# Create a new book (authenticated only)
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Creates a new book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in

    def perform_create(self, serializer):
        """
        Save the book instance.
        Custom logic could be added here (e.g., assign author based on request.user).
        """
        serializer.save()


# Update a book (authenticated only)
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<id>/update/
    Updates an existing book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Save updated book instance.
        """
        serializer.save()


# Delete a book (authenticated only)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Deletes a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
