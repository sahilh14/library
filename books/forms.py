from django import forms
from books.models import Publisher, Author

class SearchForm(forms.Form):
    title = forms.CharField()

class InsertForm(forms.Form):
    p = Publisher.objects.all()
    a = Author.objects.all()
    title = forms.CharField(max_length=100)
    publication_date = forms.DateField(required=False)
    publisher = forms.ModelChoiceField(queryset=p, empty_label='select publisher')
    authors = forms.ModelMultipleChoiceField(queryset=a)
