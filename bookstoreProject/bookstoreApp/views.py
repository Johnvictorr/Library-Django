from django.shortcuts import render, redirect
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