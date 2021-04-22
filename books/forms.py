from django import forms
from .models import Book, ISBN, Category
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class ISBNForm(forms.ModelForm):
    class Meta:
        model = ISBN
        fields = "__all__"
        exclude = ("isbn_number", )

    def clean(self):
        super(ISBNForm, self).clean()

        title = self.cleaned_data.get('title')

        if len(title) < 10 or len(title) > 50:
            raise ValidationError('Title must be between 10-50 chars')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean(self):
        super(CategoryForm, self).clean()

        name = self.cleaned_data.get('name')

        if len(name) < 2:
            raise ValidationError('Name must be at least 2 characters')
