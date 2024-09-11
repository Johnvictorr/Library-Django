from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    isbn = models.IntegerField()
    pagesNumber = models.IntegerField()
    title = models.CharField(max_length=50)
    yearPublication = models.IntegerField()
    emailPublisher = models.EmailField(max_length=254)