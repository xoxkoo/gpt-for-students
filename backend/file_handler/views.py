import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            # run the content of the file through OpenAI
            print(serializer.data)

            # TODO: this does not work - no attribute is file
            # for chunk in serializer.data.file.chunks():
            #     print(chunk)

            return Response(
                {"recreated_pdf": "here will be the summarized file"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def unique_file_name(name):
    file_extension = os.path.splitext(name)[1] if "." in name else ""
    generated_uuid = str(uuid.uuid4())
    unique_name = generated_uuid + file_extension
    return unique_name
