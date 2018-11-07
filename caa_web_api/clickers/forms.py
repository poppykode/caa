from django import forms
from .models import (
    ClickerMultipleQuestions,
)

class ClickerMultipleQuestionsForms(forms.ModelForm):
    # choices = tuple(User.objects.all().values_list())
    #courses = forms.ModelChoiceField(queryset=McCourse.objects.all())
    
    class Meta:
        model = ClickerMultipleQuestions
        fields = ('courses','question', 'optionA','optionB','optionC','optionD')