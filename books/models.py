# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

# With this manager we could accomplish something like Book.objects.title_count('some_String')
# Why would we want to add a method such as title_count()? To encapsulate commonly executed queries so that we don’t have to duplicate code.
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()    #self here refers to the manager itself


# Book.harry_objects.all() will only return the ones which have harry in the title
class HarryBookManager(models.Manager):
    def get_queryset(self):
        return super(HarryBookManager, self).get_queryset().filter(title__icontains='harry')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(null=True, blank=True)
    objects = BookManager() # replace the default manager for the model
    harry_objects = HarryBookManager() # specific to bloomsbury publisher

    def __str__(self):
        return self.title
