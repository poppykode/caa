from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from .views import (
    CourseView,CourseCategoryView,
)

urlpatterns = [
    path('courses/',CourseView),
    path('course-categories/',CourseCategoryView),
]

