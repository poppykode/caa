from django.db import models

# Create your models here.
class McCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.IntegerField()
    format = models.CharField(max_length=21)
    showgrades = models.IntegerField()
    newsitems = models.IntegerField()
    startdate = models.BigIntegerField()
    marker = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    legacyfiles = models.SmallIntegerField()
    showreports = models.SmallIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.SmallIntegerField()
    groupmodeforce = models.SmallIntegerField()
    defaultgroupingid = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requested = models.IntegerField()
    enablecompletion = models.IntegerField()
    completionnotify = models.IntegerField()
    cacherev = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_course'

    def __str__(self):
        return self.fullname 
        
class McCourseCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    coursecount = models.BigIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    timemodified = models.BigIntegerField()
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255)
    theme = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_categories'
