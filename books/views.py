# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from books.forms import InsertForm
from django.views.generic import TemplateView

def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        message = 'You searched for: %r' % request.GET['q']
        q = request.GET['q']
        obj = Book.objects.filter(title__icontains=q)
        # obj.authors.all()
        print obj
        return render(request, 'books/search_results.html', {'books': obj, 'query': q})
    else:
        message = 'You submitted an empty form'
    return HttpResponse(message)

def display(request, id):
    obj = Book.objects.get(id=id)
    return HttpResponse(obj.title)

def displayhome(request):
    print dir(request)
    return render(request, 'books/index.html')

def insert(request):
#     # import pdb; pdb.set_trace()
    if request.method == 'POST':
#         # take data from form put in in db
        form = InsertForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            b = Book(title=cd['title'],
                     publisher=cd['publisher'],
                     publication_date=cd['publication_date'])
            b.save()
            for author in cd['authors']:
                b.authors.add(author)
            print Book.objects.all()
            return render (request, 'books/inserted.html')
            # import pdb; pdb.set_trace()
    else:
        form = InsertForm()
    return render(request, 'books/insert_form.html', {'form': form})


# Inheriting TemplateView to create a generic view
class AboutView(TemplateView):
    template_name = 'books/search_form.html'
