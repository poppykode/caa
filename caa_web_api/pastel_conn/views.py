# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# from rest_framework import status
# from .models import PastelUser

# from .serializers import PastelSerilizer

# @api_view(['POST'])
# def update_pastel(request):
#     if request.method =='POST':
#         serializer = PastelSerilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
# @api_view(['GET',])
# def get_pastel_user(request):
#     if request.method == 'GET':
#         ps = PastelUser.objects.all()
#         serializer = PastelSerilizer(ps, many=True)
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET',])
# def get_pastel_user_bal(request):
#     if request.method == 'GET':
#         queryset = PastelUser.objects.all()
#         student_number = request.query_params.get('student_number', None)
#         if student_number is not None:
#             queryset = queryset.filter(student_number=student_number)
#             serializer = PastelSerilizer(queryset,many=True)
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update_pastel_user_by_stdId(request,student_number):
#     if request.method =='PUT':
#         student_number = request.query_params.get('student_number', None)
#         serializer = PastelSerilizer(student_number,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
