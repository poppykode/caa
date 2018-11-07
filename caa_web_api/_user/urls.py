from django.urls import path
from .views import (
    register_user_view,
)

app_name = 'users'
urlpatterns = [
    path('users/',register_user_view, name='user'),
]