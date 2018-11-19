from django.urls import path
from .views import PayFeesReturnView,PayFeesView

app_name = "fees"
urlpatterns = [
   path('pay_fees/', PayFeesView.as_view(), name='fees'), 
   path('fees_return/', PayFeesReturnView.as_view(), name='fees_return'), 
]