from django.db import models


class BookManager(models.Manager):

    def search_book(self, keyword):
        outcome = self.filter(title__icontains=keyword)
        return outcome

    def list_books_category(self, category):
        return self.filter(category__id=category).order_by('title')


class CategoryManager(models.Manager):

    def category_by_author(self, author):
        return self.filter(book_category__authors__id=author)        