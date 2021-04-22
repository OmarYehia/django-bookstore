from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ISBN(models.Model):
    title = models.CharField(
        max_length=50, null=False, blank=False)
    author = models.CharField(max_length=60)
    isbn_number = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Title: {self.title} | ISBN: {self.isbn_number} | Author: {self.author}"


class Book(models.Model):
    description = models.TextField(null=False, blank=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(
        ISBN, on_delete=models.CASCADE, null=True, blank=True, related_name='isbn')

    # def __str__(self):
    #     return self.isbn.author
