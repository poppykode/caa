from django.urls import path
from .views import (
    clicker_multiple_questions_create,clicker_multiple_questions_list,
    clicker_multiple_questions_api_list,clicker_multiple_answers_view,
    clicker_multiple_questions_results,
)

app_name = 'clickers'
urlpatterns = [
    path('multiple-questions/',clicker_multiple_questions_create, name='multiple-questions'),
    path('questions-list/',clicker_multiple_questions_list, name='questions-list'),
    path('multiple-questions-answers/<int:id>/',clicker_multiple_questions_results, name='questions-answers'),
    # APIs
    path('multiple-questions/list',clicker_multiple_questions_api_list),
    path('multiple-answers/post',clicker_multiple_answers_view),
    
]