from django.shortcuts import render, redirect
from .forms import BookForm, ISBNForm
from .models import Book, ISBN


def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {"books": books})


def create(request):
    if request.method == 'POST':
        return save_post_and_redirect_to_index(request)

    return show_create_book_form(request)


def create_isbn(request):
    if request.method == 'POST':
        return save_isbn_and_redirect_to_index(request)

    return show_create_isbn_form(request)


def edit(request, id):
    if request.method == 'POST':
        return edit_post_and_redirect_to_index(request, id)

    return show_edit_book_form(request, id)


def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('index')


def show(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "books/show.html", {"book": book})


# Helpers
def save_post_and_redirect_to_index(request):
    form = BookForm(request.POST)

    if not form.is_valid:
        # Handle errors here
        pass

    form.save()
    return redirect("index")


def save_isbn_and_redirect_to_index(request):
    isbn_form = ISBNForm(request.POST)

    isbn_form.save()
    return redirect("index")


def show_create_book_form(request):
    form = BookForm()

    return render(request, 'books/create.html', {'form': form})


def show_create_isbn_form(request):
    isbn_form = ISBNForm()

    return render(request, 'books/create_isbn.html', {'isbn_form': isbn_form})


def edit_post_and_redirect_to_index(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST, instance=book)

    form.save()
    return redirect("index")


def show_edit_book_form(request, id):
    try:
        book = Book.objects.get(pk=id)
        form = BookForm(instance=book)

        return render(request, 'books/edit.html', {
            'form': form,
            'book': book
        })
    except Exception as e:
        print(e)
        return render(request, "books/404.html")
