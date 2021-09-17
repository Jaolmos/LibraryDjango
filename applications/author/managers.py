from django.db import models

class AuthorManager(models.Manager):
    
    def search_author(self, kword):
        outcome = self.filter(first_name__icontains=kword)
        
        return outcome