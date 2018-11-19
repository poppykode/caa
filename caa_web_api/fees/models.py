from django.db import models

# Create your models here.
class Transaction(models.Model):
    student_number = models.CharField(max_length=255, blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    reference = models.CharField(max_length=255, blank=True)
    pollurl = models.CharField(max_length=255, blank=True)
    paynowreference = models.CharField(max_length=255, blank=True)
    amount = models.FloatField(default=0)
    email = models.EmailField(max_length=255, blank=True) 
    requesting_number = models.CharField(max_length=255, blank=True) 
    fullname =  models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['date']
   