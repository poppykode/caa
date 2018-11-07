from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import McUser
from .serializers import McUserSerilizer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def register_user_view(request):
    """
    List all  users, or create a new a new user.
    """
    if request.method == 'GET':
        users = McUser.objects.all()
        serializer = McUserSerilizer(users,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = McUserSerilizer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



