from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from file_handler.models import UploadedFile
from common.utils import query_file
from .serializers import FileQueryAnswerSerializer

# Create your views here.


class FileQueryView(APIView):
    def get(self, request, format=None):
        # get the file path from DB
        try:
            file_id = request.query_params.get("fileId")
            query = request.query_params.get("query")

            uploaded_file = UploadedFile.objects.get(pk=file_id)
        except UploadedFile.DoesNotExist:
            return Response("File not found", status=status.HTTP_404_NOT_FOUND)

        # query the file
        result = query_file(filePath=uploaded_file.file.name, query=query)

        # save the data
        serializer = FileQueryAnswerSerializer(
            data={"fileId": file_id, "query": query, "answer": result}
        )
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(
                "Error while saving FileQueryAnswer",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # return the result
        return Response(result, status=status.HTTP_200_OK)
