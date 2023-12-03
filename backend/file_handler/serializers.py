from rest_framework import serializers
from .models import UploadedFile

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('title', 'file')

    # Make the 'title' field optional
    title = serializers.CharField(max_length=255, required=False)