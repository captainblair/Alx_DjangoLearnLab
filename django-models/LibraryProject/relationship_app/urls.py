from django.urls import path
from .views import list_books, LibraryDetailView, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('books/add/', add_book, name='add-book'),
    path('books/<int:pk>/edit/', edit_book, name='edit-book'),
    path('books/<int:pk>/delete/', delete_book, name='delete-book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]
