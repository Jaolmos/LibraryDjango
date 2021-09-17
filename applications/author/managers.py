from django.db import models

class AuthorManager(models.Manager): #managers for the author model

    def search_author(self, kword):
        outcome = self.filter(first_name__icontains=kword)
        
        return outcome