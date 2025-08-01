# api/views.py

# Add 'viewsets' to this import
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# This is the old view from the previous task
class BookList(generics.ListAPIView):
    """
    API view to retrieve a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Add this new ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer