from rest_framework import serializers
from .models import FileQueryAnswer

class FileQueryAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileQueryAnswer
        fields = ('fileId', 'query', 'answer')

    # Make the 'title' field optional
    fileId = serializers.IntegerField(required=True)
    query = serializers.CharField(required=True)
    answer = serializers.CharField(required=True)