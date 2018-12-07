from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LibraryForms
from .models import Library
from .serializers import LibrarySerilizer

# Create your views here.
@login_required
def library_book_create(request):
    if request.method == 'POST':
        form_library = LibraryForms(request.POST,request.FILES)
        if form_library.is_valid():
            new_form = form_library.save(commit=False)
            new_form.user = request.user
            form_library .save()
            messages.success(request, 'Book has been successfully created!')
            return redirect('library:library-list')
    else:
        form_library = LibraryForms()
    return render(request,'library/library_create.html',{'form_library':form_library })

@login_required
def library_book_list (request):
    library = Library.objects.all()
    data = {}
    data['book_list'] = library
    return render(request,'library/library_book_list.html',data)

@api_view(['GET',])
def library_book_list_api_list(request):
    if request.method == 'GET':
        library = Library.objects.all()
        serializer = LibrarySerilizer(library, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


