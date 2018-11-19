from rest_framework import serializers
from .models import Library
class LibrarySerilizer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source='courses')
    class Meta:
        model = Library
        fields = ('courses', 'title', 'author', 'subject', 'book_file','cover_image') 