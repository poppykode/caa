from django import forms
from .models import (
    Orientation,
)

class OrientationForms(forms.ModelForm):
 
    class Meta:
        model = Orientation
        fields = ('title','priority','video','cover_image')