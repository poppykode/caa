from django.urls import path
from .views import (
    library_book_create,library_book_list,
    library_book_list_api_list,library_book_delete,
    book_update,
)

app_name ='library'
urlpatterns = [
    path('create/',library_book_create, name='library-create'),
    path('delete/<int:pk>',library_book_delete , name='book-delete'),
    path('edit/<int:pk>',book_update, name='book-update'),
    path('list-admin/',library_book_list,name='library-list'),
    path('list/',library_book_list_api_list),
]