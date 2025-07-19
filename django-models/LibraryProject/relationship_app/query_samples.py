from relationship_app.models import Author, Book, Library

# Query all books by a specific author
author_name = "George Orwell"

# Get the author object
author = Author.objects.get(name=author_name)

# Get all books written by that author
books_by_author = Book.objects.filter(author=author)

# Print the book titles
for book in books_by_author:
    print(book.title)

# Query all books in a library
library_name = "Main Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)