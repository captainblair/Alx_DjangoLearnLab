from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Library

@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Dummy logic for simplicity
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    # Dummy logic for simplicity
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    # Dummy logic for simplicity
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'delete_book.html', {'book': book})

from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
