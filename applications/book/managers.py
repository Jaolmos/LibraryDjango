from django.db import models

from django.db.models import Q

class BookManager(models.Manager):

    def search_book(self, keyword):
        outcome = self.filter(title__icontains=keyword)
        
        return outcome

    '''def search_book2(self, keyword):
        outcome = self.filter(
            Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword)
            )
        
        return outcome'''