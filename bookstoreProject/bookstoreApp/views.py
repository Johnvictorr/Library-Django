from django.shortcuts import render
from django.forms import ModelForm
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'publisher', 'isbn', 'pagesNumber', 'title', 'yearPublication', 'emailPublisher']

def bookList(request, template_name='bookList.html'):
    book = Book.objects.all()
    books = {'list': book}
    return render(request, template_name, books)