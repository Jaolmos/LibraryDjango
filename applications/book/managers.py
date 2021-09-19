from django.db import models


class BookManager(models.Manager):

    def search_book(self, keyword):
        outcome = self.filter(title__icontains=keyword)
        
        return outcome

    def list_books_category(self, category):

        return self.filter(category__id=category).order_by('title')