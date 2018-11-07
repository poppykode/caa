from django.db import models
from django.contrib.auth.models import User
from courses_grades.models import McCourse

# Create your models here.

class ClickerMultipleQuestions(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    courses = models.ForeignKey(McCourse,null=True,on_delete=models.CASCADE)
    question =  models.CharField(max_length=255)
    optionA = models.CharField(max_length=255)
    optionB =  models.CharField(max_length=255)
    optionC = models.CharField(max_length=255)
    optionD =  models.CharField(max_length=255)