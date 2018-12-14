from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from rest_framework import status

from .serializers import PastelSerilizer

@api_view(['POST'])
def update_pastel(request):
    if request.method =='POST':
        serializer = PastelSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
