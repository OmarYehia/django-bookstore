from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('create_isbn', views.create_isbn, name='create_isbn'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('books/<int:id>', views.show, name="show"),
]
