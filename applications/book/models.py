from django.db import models

from applications.author.models import Author

from .managers import BookManager, CategoryManager


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    objects = CategoryManager()
    
    def __str__(self):
        return str(self.id) + '-' + self.name

class Book(models.Model):
    title = models.CharField(max_length=60, verbose_name='Title')
    category = models.ForeignKey(
    Category, on_delete=models.CASCADE,
    verbose_name='Category',
    related_name = 'book_category'
    )
    authors = models.ManyToManyField(Author, verbose_name='Autor')
    date = models.DateField(verbose_name='Release date')  
    book_cover = models.ImageField(verbose_name='Book cover', upload_to='Image')     
    visits = models.PositiveIntegerField(verbose_name='Visits')


    objects = BookManager()

    def __str__(self):
        return  str(self.id) + '-' + self.title
