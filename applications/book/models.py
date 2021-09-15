from django.db import models

from applications.author.models import Author

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Libro(models.Model):
    title = models.CharField(max_length=60, verbose_name='Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    authors = models.ManyToManyField(Author, verbose_name='Autor')
    date = models.DateField(verbose_name='Release date')  
    book_cover = models.ImageField(verbose_name='Book cover', upload_to='Image')     
    visits = models.PositiveIntegerField(verbose_name='Visits')

    def __str__(self):
        return self.title
