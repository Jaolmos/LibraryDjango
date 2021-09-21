from django.db import models


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