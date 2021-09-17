from django.db import models

class AuthorManager(models.Manager):

    def search_author(self, keyword):
        outcome = self.filter(first_name__icontains=keyword)
        
        return outcome