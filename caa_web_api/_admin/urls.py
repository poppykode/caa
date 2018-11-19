from django.urls import path
from django.urls import include
from django.conf.urls import url
from .views import (
   DashboardView,RegisterView,
   StuffMembersListView,disable_user_view,
)
app_name = '_admin'
urlpatterns = [
    path('dashboard/',DashboardView),
    path('register/',RegisterView, name='register'),
    path('stuff-members/',StuffMembersListView.as_view(), name='stuff-members'),
    path('stuff-member/<str:user>/disable/',disable_user_view,name="stuff-member-disable"),
]
