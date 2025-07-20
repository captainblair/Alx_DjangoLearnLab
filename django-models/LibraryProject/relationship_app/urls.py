from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book-list'),
    path('books/add/', views.add_book, name='add-book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit-book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete-book'),
]
