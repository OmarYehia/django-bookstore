from django.contrib import admin
from .models import Book, ISBN, Category
from .forms import ISBNForm, CategoryForm, BookForm


class BookInline(admin.StackedInline):
    model = Book
    max_num = 2
    extra = 1


class ISBNAdmin(admin.ModelAdmin):
    form = ISBNForm
    list_display = ('isbn_number', 'title', 'author')
    inlines = [BookInline]


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('isbn', 'description',)
    list_filter = ('categories',)
    search_fields = ('isbn.title', )


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm


admin.site.register(Book, BookAdmin)
admin.site.register(ISBN, ISBNAdmin)
admin.site.register(Category, CategoryAdmin)
