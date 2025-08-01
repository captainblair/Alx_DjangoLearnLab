from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profiles/", null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title
