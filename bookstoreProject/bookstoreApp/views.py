from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'publisher', 'isbn', 'pagesNumber', 'title', 'yearPublication', 'emailPublisher']


def bookList(request):
    book = Book.objects.all()
    books = {'list': book}
    return render(request, 'bookList.html', books)


def newBook(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listBooks')
    return render(request, 'booksForm.html', {'form': form})


def editBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('listBooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'booksForm.html', {'form': form})


def deleteBook(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('listBooks')
    return render(request, 'deleteBook.html', {'book': book})