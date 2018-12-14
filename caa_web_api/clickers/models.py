from django.db import models
from django.contrib.auth.models import User
from courses_grades.models import McCourse

# Create your models here.

class ClickerMultipleQuestions(models.Model):
    # COURSES = (
    #     ('accounting', 'accounting'),
    #     ('auditing', 'auditing'),
    # )
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    # courses = models.CharField(max_length=30, choices=COURSES, default='Please Course')
    courses = models.ForeignKey(McCourse,null=True,on_delete=models.CASCADE)
    question =  models.CharField(max_length=255)
    optionA = models.CharField(max_length=255)
    optionB =  models.CharField(max_length=255)
    optionC = models.CharField(max_length=255)
    optionD =  models.CharField(max_length=255)

    def  __str__(self): 
        return self.courses 

class ClickerMultipleQuestionsAnswers(models.Model):
    # question_id
    question =  models.ForeignKey(ClickerMultipleQuestions,null=True,on_delete=models.CASCADE)
    course_id = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

 


