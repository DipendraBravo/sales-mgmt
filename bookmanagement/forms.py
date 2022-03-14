from django import forms
from .models import Book, UserRequest
from django.forms import fields
from django.forms import ModelForm


class BookCreation(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'author', 'edition', 'unitprice', 'in_stock', 'image')

        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'edition': forms.TextInput(attrs={'class': 'form-control'}),
            'unitprice': forms.NumberInput(attrs={'class': 'form-control'}),
            'in_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UserRequestForm(forms.ModelForm):

    class Meta:
        model = UserRequest
        # fields = ('username', 'address', 'contact', 'book_quantity', 'delivered_status','book')
        fields = '__all__'

        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'book_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

