from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def library_book_delete(request, pk):
    book= get_object_or_404(Library, pk=pk)    
    if request.method=='POST':
        book.delete()
        messages.success(request, 'Book has been successfully Deleted!')
        return redirect('library:library-list')
    return render(request,'library/book_confirm_delete.html', {'data':book})

@login_required
def book_update(request, pk):
    bk= get_object_or_404(Library, pk=pk)
    if request.method =='POST':
        form_library = LibraryForms(request.POST,request.FILES,instance=bk)
        if form_library.is_valid():                          
            form_library.save()
            messages.success(request, 'Book has been successfully updated!')
            return redirect('library:library-list')
    else:     
        context = {'form_library': LibraryForms(instance=bk)}
    return render(request, 'library/book_update.html', context)

@api_view(['GET',])
def library_book_list_api_list(request):
    if request.method == 'GET':
        library = Library.objects.all()
        print(library)
        serializer = LibrarySerilizer(library, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


