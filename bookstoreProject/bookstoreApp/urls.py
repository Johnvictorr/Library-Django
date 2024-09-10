from django.urls import path
from .views import *

urlpatterns = [
    path('bookList/', bookList, name='listBooks'),
]
