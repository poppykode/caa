from rest_framework import serializers
from .models import (
    McUser,
)

class McUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = McUser
        fields = (
            'id', 'auth', 'confirmed', 'policyagreed', 'deleted','suspended',
            'mnethostid','username','password','idnumber','firstname','lastname','email',
            'emailstop','lang','calendartype'
            ) 