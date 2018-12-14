from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrientationForms
from django.contrib import messages
from .models import Orientation,RegNumbers,Sectionb,First
from rest_framework.decorators import api_view
from .serializers import OrientationSerilizer,RegNumberSerilizer,SectionbSerilizer,FirstSerilizer
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
@login_required
def create_orientation_video(request):
    if request.method == 'POST':
        form_orientation = OrientationForms(request.POST,request.FILES)
        if form_orientation.is_valid():
            form_orientation.save()
            messages.success(request, 'orientation video has been successfully created!')
            return redirect('orientation:orientation-list')
    else:
        form_orientation= OrientationForms()
    return render(request,'orientation/orientation_create.html',{'form_orientation':form_orientation })

@login_required
def view_orientation_video(request):
    orientation = Orientation.objects.all()
    data = {}
    data['orientation_list'] = orientation
    return render(request,'orientation/orientation_list.html',data)

@login_required
def video_delete(request, pk):
    # orientation= get_object_or_404(Orientation, pk=pk)  
    orientation = Orientation.objects.filter(pk=pk)  
    if request.method=='POST':
        orientation.delete()
        messages.success(request, 'Video has been successfully Deleted!')
        return redirect('orientation:orientation-list')
    return render(request,'orientation/video_confirm_delete.html', {'data':orientation})

@login_required
def video_update(request, pk):
    vid= get_object_or_404(Orientation, pk=pk)
    if request.method =='POST':
        form = OrientationForms(request.POST,request.FILES,instance=vid)
        if form.is_valid():                          
            form.save()
            messages.success(request, 'Video has been successfully updated!')
            return redirect('orientation:orientation-list')
    else:     
        context = {'form': OrientationForms(instance=vid)}
    return render(request, 'orientation/video_update.html', context)

def video_update_post(request, pk):
    if request.method=='POST':
        form = Orientation(request.POST,request.FILES)
        if form.is_valid():        
            form.save()
            messages.success(request, 'Video has been successfully updated!')
            return redirect('orientation:orientation-list')
    else:
        form = Orientation()
    return render(request, 'orientation/video_update.html', {'form':form})


@api_view(['GET',])
def orientation_list_api_list(request):
    if request.method == 'GET':
        orientation = Orientation.objects.all()
        serializer = OrientationSerilizer(orientation, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_reg_numbers(request):
    if request.method == 'GET':
        queryset = RegNumbers.objects.using('students').all()
        student_number = request.query_params.get('student_number', None)
        if student_number is not None:
            queryset = queryset.filter(student_number=student_number)
            serializer = RegNumberSerilizer(queryset,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_student_info(request):
    if request.method == 'GET':
        queryset  = Sectionb.objects.using('students').all()
        username = request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)    
            serializer = SectionbSerilizer(queryset ,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_student_info_pass(request):
    if request.method == 'GET':
        queryset  = First.objects.using('students').all()
        username = request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)    
            serializer = FirstSerilizer(queryset ,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

