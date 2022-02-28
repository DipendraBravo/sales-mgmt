from django import forms
from .models import Book
from django.forms import fields
from django.forms import ModelForm


class BookCreation(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('book_name',
                  'author',
                  'edition',
                  'unitprice',
                  'in_stock',
                  'image',
                  )
