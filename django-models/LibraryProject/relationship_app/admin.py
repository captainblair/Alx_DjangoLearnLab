from django.contrib import admin
from .models import Book, Library, UserProfile

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(UserProfile)
