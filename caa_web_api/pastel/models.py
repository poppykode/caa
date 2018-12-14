from django.db import models

# Create your models here.
class PastelUser (models.Model):
    username =  models.CharField(max_length=255,blank=True, null=True)
    student_number =  models.CharField(max_length=255,blank=True, null=True)
    fullname = models.CharField(max_length=255,blank=True, null=True)
    date_of_transaction =  models.CharField(max_length=255,blank=True, null=True)
    reference_number =  models.CharField(max_length=255,blank=True, null=True)
    amount = models.CharField(max_length=255)
    requesting_number =  models.CharField(max_length=255,blank=True, null=True)

    def  __str__(self): 
        return self.username 

    class Meta:
        ordering = ['username']


