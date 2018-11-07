from rest_framework import serializers
from .models import (
    ClickerMultipleQuestions,
)

class ClickerMultipleQuestionSerilizer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='courses')
    class Meta:
        model = ClickerMultipleQuestions
        fields = ('id', 'question', 'optionA', 'optionB', 'optionC','optionD','course_name') 