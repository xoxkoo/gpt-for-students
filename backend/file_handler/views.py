import uuid
import os
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer
from ..common.utils import summarizeFile, generatePdf
from django.http import FileResponse

###
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file = serializer.validated_data["file"]

            # split pdf into text chunks
            if uploaded_file is not None:
                file_extension = os.path.splitext(uploaded_file.name)[1][1:]

                if file_extension.lower() == "pdf":
                    file_name = os.path.splitext(uploaded_file.name)[0]

                    # If not title, give it the file name value
                    if (
                        "title" in serializer.validated_data
                        and serializer.validated_data["title"]
                    ):
                        pass
                    else:
                        serializer.validated_data["title"] = file_name

                    # give file unique name
                    serializer.validated_data["file"].name = unique_file_name(
                        serializer.validated_data["file"].name
                    )

                    # save file
                    saved_file = serializer.save()
                else:
                    return Response(
                        saved_file.id, status=status.HTTP_400_BAD_REQUEST
                    )

            return Response(
                       {"id": saved_file.id}, status=status.HTTP_200_OK
                    )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def unique_file_name(name):
    file_extension = os.path.splitext(name)[1] if "." in name else ""
    generated_uuid = str(uuid.uuid4())
    unique_name = generated_uuid + file_extension
    return unique_name
