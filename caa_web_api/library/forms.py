from django import forms
from .models import (
    Library,
)

class LibraryForms(forms.ModelForm):
 
    class Meta:
        model = Library
        fields = ('courses','title', 'author','subject','book_file','cover_image')