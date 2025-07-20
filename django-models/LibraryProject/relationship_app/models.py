from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)

    class Meta:
        permissions = [
            ("canaddbook", "Can add book"),
            ("canchangebook", "Can change book"),
            ("candeletebook", "Can delete book"),
        ]

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
