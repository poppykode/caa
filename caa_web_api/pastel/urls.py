from django.urls import path
from .views import update_pastel

app_name = 'pastel'
urlpatterns = [
    path('update/',update_pastel, name='pastel-update'),
 
]