from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN


@receiver(post_save, sender=Book)
def after_book_creation(sender, instance, created, *args, **kwargs):
    if created:

        ISBN_instance = ISBN.objects.create(
            author=instance.author,
            title=instance.title)

        ISBN_instance.save()
        instance.isbn = ISBN_instance
        instance.save()
