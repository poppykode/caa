from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    ClickerMultipleQuestions,
)
from .forms import (
    ClickerMultipleQuestionsForms,
)
from .serializers import (
    ClickerMultipleQuestionSerilizer
)

# Create your views here.
@login_required
def clicker_multiple_questions_create(request):
    if request.method == 'POST':
        form_clickers = ClickerMultipleQuestionsForms(request.POST)
        if form_clickers.is_valid():
            new_form = form_clickers.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Question has been successfully created!')
            return redirect('clickers:multiple-questions')
    else:
        form_clickers = ClickerMultipleQuestionsForms()
    return render(request,'clickers/clickers_multiple.html',{'form_clickers':form_clickers })


@login_required
def clicker_multiple_questions_list (request):
    user = self.request.user
    clickers = ClickerMultipleQuestions.objects.filter(user=user)
    data = {}
    data['clickers_list'] = clickers
    return render(request,'clickers/clickers_list.html',data)

#Enpointpoint

@api_view(['GET',])
def clicker_multiple_questions_api_list(request):
    if request.method == 'GET':
        clickers = ClickerMultipleQuestions.objects.all()
        serializer = ClickerMultipleQuestionSerilizer(clickers, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
