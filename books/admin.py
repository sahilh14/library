# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from books.models import Publisher, Book, Author

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
