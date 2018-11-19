from django.urls import path
from .views import (
    library_book_create,library_book_list,
    library_book_list_api_list,
)

app_name ='library'
urlpatterns = [
    path('create/',library_book_create, name='library-create'),
    path('list-admin/',library_book_list,name='library-list'),
    path('list/',library_book_list_api_list),
]