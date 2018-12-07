from django.db import models
from django.contrib.auth.models import User
from courses_grades.models import McCourse

# Create your models here.
class Library (models.Model):
    COURSES = (
        ('accounting', 'accounting'),
        ('auditing', 'auditing'),
    )
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    courses = models.CharField(max_length=30, choices=COURSES, default='Please Course')
    # courses = models.ForeignKey(McCourse,null=True,on_delete=models.CASCADE)
    title =  models.CharField(max_length=255)
    author =  models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    book_file =  models.FileField(upload_to='books/',null=True, blank =False,)
    cover_image =  models.FileField(upload_to='cover_images/',null=True, blank =False,)

    def  __str__(self): 
        return self.courses 
