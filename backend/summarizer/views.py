from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from file_handler.models import UploadedFile
from backend.common.utils import summarizeFile, generatePdf
from django.http import FileResponse

# Create your views here.

class FileSummarizeView(APIView):
    def get(self, fileId, format=None):
        #get the file path from DB
        try:
            uploaded_file = UploadedFile.objects.get(pk=fileId)
        except UploadedFile.DoesNotExist:
            return Response("File not found", status=status.HTTP_404_NOT_FOUND)
        
        #summarize the file
        summarized_context = summarizeFile(f"files/{uploaded_file.file}")

        generated_pdf = generatePdf(summarized_context)

        #return the result
        return FileResponse(
                generated_pdf, as_attachment=True, filename=f"{uploaded_file.title}.pdf"
            )