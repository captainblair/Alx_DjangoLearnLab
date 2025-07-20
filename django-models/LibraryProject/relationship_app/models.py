from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=100, default="Default Library")  # default to avoid migration prompt
    location = models.CharField(max_length=255, default="Unknown Location")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Unknown Author")  # avoids "author needs default" error
    library = models.ForeignKey(Library, on_delete=models.CASCADE, default=1)  # avoids "library needs default" error

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, default="No bio")

    def __str__(self):
        return self.user.username
