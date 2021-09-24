from django.db import models
from django.db.models.aggregates import Avg


class LoanManager(models.Manager):
    
    def average_book_ages(self):
        outcome = self.filter(book__id='2').aggregate(average_age=Avg('reader__age'))
        return outcome
