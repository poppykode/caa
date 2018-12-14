from rest_framework import serializers
from .models import (
    Orientation,RegNumbers,Sectionb,First,
)
class OrientationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Orientation
        fields = ('title','priority', 'cover_image', 'video') 

class RegNumberSerilizer(serializers.ModelSerializer):
    class Meta:
        model = RegNumbers
        fields = ('student_number','entry_mode', 'username') 

class SectionbSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Sectionb
        fields = ('first_name','last_name','id_number',
        'dob','cell_number','address','next_fullname','next_num','next_email_address',
        'org_name','position','institution','year','qualification',
        )

class FirstSerilizer(serializers.ModelSerializer):
    class Meta:
        model = First
        fields = ('username','password','enrolment_type','classes',)
