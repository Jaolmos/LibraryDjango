from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Book
from . managers import BookManager

class ListBooks(ListView):
    context_object_name = 'list_books'
    template_name = 'book/list-books.html'

    def get_queryset(self):
        kword = self.request.GET.get('keyword','')
        return Book.objects.search_book(kword)


class ListBooks2(ListView):
    context_object_name = 'list_books'
    template_name = 'book/list-books2.html'

    def get_queryset(self):
        return Book.objects.list_books_category('2')



class BookDetailView(DetailView):
    model = Book
    template_name = "book/detail.html"
