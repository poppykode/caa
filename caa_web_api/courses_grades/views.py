from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses_grades.models import (
                McCourse,McCourseCategories,
                ) 
from .serializers import(
     McCourseSerializer, McCourseCategoriesSerializer,
     )

from rest_framework.permissions import (
    AllowAny,
    )

@api_view(['GET',])
def CourseView(request):
    if request.method == 'GET':
        courses = McCourse.objects.all()
        serializer = McCourseSerializer(courses, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def CourseCategoryView(request):
    if request.method == 'GET':
        courses_categories = McCourseCategories.objects.all()
        serializer = McCourseCategoriesSerializer(courses_categories, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


