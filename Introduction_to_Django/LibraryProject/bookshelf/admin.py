from django.contrib import admin
from .models import Book  # Import the Book model

# Register the model with custom admin settings
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these columns
    list_filter = ('publication_year',)  # add filter by year
    search_fields = ('title', 'author')  # add search by title or author
