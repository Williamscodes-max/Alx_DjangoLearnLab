from django import forms
from .models import Book

# Form to create/edit a Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
