from rest_framework import serializers
from .models import (
    ClickerMultipleQuestions,ClickerMultipleQuestionsAnswers,
)

class ClickerMultipleQuestionSerilizer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source='courses')
    class Meta:
        model = ClickerMultipleQuestions
        fields = ('id', 'question', 'optionA', 'optionB', 'optionC','optionD','courses') 

class ClickerMultipleQuestionsAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickerMultipleQuestionsAnswers
        fields = ('question', 'course_id', 'answer') 