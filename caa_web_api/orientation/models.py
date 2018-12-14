from django.db import models

# Create your models here.
class Orientation (models.Model):
    title =  models.CharField(max_length=255)
    priority = models.PositiveIntegerField(default=1)
    cover_image =  models.FileField(upload_to='cover_images/',null=True, blank =False,)
    video =  models.FileField(upload_to='video/',null=True, blank =False,)
    
    def  __str__(self): 
        return self.title 

    class Meta:
        ordering = ['priority']

class First(models.Model):
    username = models.CharField(unique=True, max_length=220)
    password = models.CharField(max_length=120)
    enrolment_type = models.CharField(max_length=120)
    classes = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'first'

class RegNumbers(models.Model):
    student_number = models.CharField(unique=True, max_length=6)
    entry_mode = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    old_student_numbers = models.CharField(max_length=11)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reg_numbers'

class Sectionb(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    dob = models.CharField(max_length=20)
    duty = models.TextField()
    position = models.CharField(max_length=120)
    org_name = models.CharField(max_length=120)
    qualification = models.TextField()
    year = models.CharField(max_length=120)
    institution = models.CharField(max_length=200)
    qualification1 = models.TextField()
    institution1 = models.CharField(max_length=120)
    year1 = models.CharField(max_length=120)
    institute11 = models.TextField()
    year11 = models.TextField()
    qualification11 = models.TextField()
    institute12 = models.TextField()
    year12 = models.TextField()
    qualification12 = models.TextField()
    institute13 = models.TextField()
    year13 = models.TextField()
    qualification13 = models.TextField()
    institute14 = models.TextField()
    year14 = models.TextField()
    qualification14 = models.TextField()
    prev_org_name = models.CharField(max_length=200)
    prev_position = models.CharField(max_length=200)
    prev_duty = models.TextField()
    cell_number = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    email_address = models.CharField(unique=True, max_length=120)
    country = models.CharField(max_length=120)
    gender = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    id_number = models.CharField(max_length=50)
    next_fullname = models.CharField(max_length=300)
    next_relation = models.CharField(max_length=300)
    next_num = models.CharField(max_length=300)
    next_email_address = models.CharField(max_length=300)
    disability = models.CharField(max_length=300)
    dis_details = models.CharField(max_length=300)
    town = models.CharField(max_length=300)
    payer = models.CharField(max_length=300)
    payee_name = models.CharField(max_length=300)
    payee_number = models.CharField(max_length=300)
    payee_email = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sectionb'


