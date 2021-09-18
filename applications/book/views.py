from django.shortcuts import render
from django.views.generic import ListView
from . models import Book
from . managers import BookManager

class ListBooks(ListView):
    context_object_name = 'list_books'
    template_name = 'book/list-books.html'

    def get_queryset(self):
        kword = self.request.GET.get('keyword','')
        return Book.objects.search_book(kword)