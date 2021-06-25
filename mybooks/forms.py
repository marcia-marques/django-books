from django import forms

from .models import Book


class DateInput(forms.DateInput):
    input_type = 'date'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title',
                  'author',
                  'date',
                  'epub',
                  'cover']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'author': forms.TextInput(attrs={'class': 'form-control'}),
                   'date': DateInput(attrs={'class': 'form-control'}),
                   'epub': forms.FileInput(attrs={'class': 'form-control'}),
                   'cover': forms.FileInput(attrs={'class': 'form-control'})}
