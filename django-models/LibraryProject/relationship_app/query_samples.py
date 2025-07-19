from .models import Author, Book, Library, Librarian

# List all books in a library
def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.book_set.all()

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    return Librarian.objects.get(library__id=library_id)
