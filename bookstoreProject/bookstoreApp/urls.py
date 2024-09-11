from django.urls import path
from .views import *

urlpatterns = [
    path('bookList/', bookList, name='listBooks'),
    path('newBook/', newBook, name='newBook'),
    path('editBook/<int:pk>/', editBook, name='editBook'),
    path('deleteBook/<int:pk>/', deleteBook, name='deleteBook'),
]
