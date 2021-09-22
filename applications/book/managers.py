from django.db import models
from django.db.models.aggregates import Count


class BookManager(models.Manager):

    def search_book(self, keyword):
        outcome = self.filter(title__icontains=keyword)
        return outcome

    def list_books_category(self, category):
        return self.filter(category__id=category).order_by('title')

    def add_author_book(self, book_id, author):
        book = self.get(id=book_id) 
        book.authors.add(author)
        return book


class CategoryManager(models.Manager):

    def category_by_author(self, author):
        return self.filter(book_category__authors__id=author).distinct()   

    def list_category_books(self):
        outcome = self.annotate(number_of_books=Count('book_category'))
        for o in outcome:
            print('**********')
            print(o, o.book_category)
        return outcome
            
        