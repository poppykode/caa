from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    ClickerMultipleQuestions,ClickerMultipleQuestionsAnswers,
)
from .forms import (
    ClickerMultipleQuestionsForms,
)
from .serializers import (
    ClickerMultipleQuestionSerilizer,ClickerMultipleQuestionsAnswersSerializer,
)

# Create your views here.
@login_required
def clicker_multiple_questions_create(request):
    if request.method == 'POST':
        form_clickers = ClickerMultipleQuestionsForms(request.POST)
        if form_clickers.is_valid():
            new_form = form_clickers.save(commit=False)
            new_form.user = request.user
            form_clickers.save()
            messages.success(request, 'Question has been successfully created!')
            return redirect('clickers:multiple-questions')
    else:
        form_clickers = ClickerMultipleQuestionsForms()
    return render(request,'clickers/clickers_multiple.html',{'form_clickers':form_clickers })


@login_required
def clicker_multiple_questions_list (request):
    user = request.user
    user_id =user.id
    clickers = ClickerMultipleQuestions.objects.filter(user_id=user_id)
    data = {}
    data['clickers_list'] = clickers
    return render(request,'clickers/clickers_list.html',data)

@login_required
def clicker_multiple_questions_results (request,id):

    optionA = ClickerMultipleQuestionsAnswers.objects.filter(answer='optionA').count() 
    optionB = ClickerMultipleQuestionsAnswers.objects.filter(answer='optionB').count()
    optionC = ClickerMultipleQuestionsAnswers.objects.filter(answer='optionC').count()
    optionD = ClickerMultipleQuestionsAnswers.objects.filter(answer='optionD').count()
    data = {}
    data['optionA'] = optionA
    data['optionB'] = optionB
    data['optionC'] = optionC
    data['optionD'] = optionD
    print(data)
    return render(request,'clickers/clickers_results.html',data)

#Enpointpoint

@api_view(['GET',])
def clicker_multiple_questions_api_list(request):
    if request.method == 'GET':
        clickers = ClickerMultipleQuestions.objects.all()
        serializer = ClickerMultipleQuestionSerilizer(clickers, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def clicker_multiple_answers_view(request):
    if request.method =='POST':
        serializer = ClickerMultipleQuestionsAnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
