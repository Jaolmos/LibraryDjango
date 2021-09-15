from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=60,verbose_name='First name')
    last_name = models.CharField(max_length=60, verbose_name='Last name')
    nationality = models.CharField(max_length=40, verbose_name='Nacionality')
    age = models.PositiveIntegerField(verbose_name='Age', default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
