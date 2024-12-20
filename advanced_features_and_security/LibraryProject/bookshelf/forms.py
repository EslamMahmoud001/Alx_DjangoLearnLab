from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1000, 'max': 9999}),
        }

    # You can add additional custom validation here if necessary