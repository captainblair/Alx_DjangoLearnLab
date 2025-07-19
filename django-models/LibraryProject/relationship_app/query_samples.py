# relationship_app/query_samples.py

from relationship_app.models import Library

# Replace 'library_name' with the actual name of the library you want to query
library_name = "Main Library"

# Get the Library object by name
library = Library.objects.get(name=library_name)

# List all books in that library
books_in_library = library.books.all()

# Print out the book titles
for book in books_in_library:
    print(book.title)