# api/views.py

from rest_framework import generics, viewsets
# Add 'permissions' to this import
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

# This view remains unchanged and open
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This is the ViewSet we will secure
class BookViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    It is protected by TokenAuthentication and only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Add this line to enforce authentication for this ViewSet
    permission_classes = [permissions.IsAuthenticated]