from rest_framework import serializers
from .models import (
   PastelUser,
)
class PastelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PastelUser
        fields = ('username','fullname','student_number','date', 'reference_number','amount','requesting_number') 