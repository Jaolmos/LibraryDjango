from django.shortcuts import render

from django.views.generic import ListView

from . models import Author

class ListAuthors(ListView):
    context_object_name = 'list_authors'
    template_name = 'author/list.html'

    def get_queryset(self):
        kword = self.request.GET.get('keyword','')
        return Author.objects.search_author(kword)

