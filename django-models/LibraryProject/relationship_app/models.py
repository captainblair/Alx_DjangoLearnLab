from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
