from django.db import models

from django.db.models import Q

class AuthorManager(models.Manager):

    def search_author(self, keyword):
        outcome = self.filter(first_name__icontains=keyword)
        
        return outcome

    def search_author2(self, keyword):
        outcome = self.filter(
            Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword)
            )
        
        return outcome