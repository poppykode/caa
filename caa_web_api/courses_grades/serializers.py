from rest_framework import serializers
from .models import (
    McCourse,McCourseCategories,
)

class McCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = McCourse
        fields = ('id', 'category', 'fullname', 'shortname', 'startdate') 

class McCourseCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = McCourseCategories
        fields = ('id', 'name', 'coursecount') 