from django.db import models

from applications.book.models import Book

class Reader(models.Model):
    first_name = models.CharField(max_length=60,verbose_name='First name')
    last_name = models.CharField(max_length=60, verbose_name='Last name')
    nationality = models.CharField(max_length=40, verbose_name='Nacionality')
    age = models.PositiveIntegerField(verbose_name='Age',default=0)

    def __str__(self):
        return self.first_name 


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    returned_book = models.BooleanField()
    
    def __str__(self):
        return self.book.title
