import io
import uuid
import os
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer
from .utils import summarizeFile, generatePdf, get_pdf_text, unique_file_name, get_text_chunks,get_vectorstore
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
                    file_name = serializer.validated_data["file"].name

                    # save file
                    serializer.save()

                    print(file_name)

                    print(get_vectorstore(get_text_chunks(get_pdf_text(f"files/{file_name}"))).similarity_search('Who is author?')[0])
                    # summarize the pdf
                    # try:
                    #     summarized_context = summarizeFile(
                    #         f"files/{file_name}"
                    #     )
                    # except:
                    #     return Response(
                    #         "Could not summarize PDF", status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    #     )
                    summarized_context = ''

                    # generated_pdf = generatePdf(summarized_context)

                    return Response(summarized_context, status=status.HTTP_200_OK)
                else:
                    return Response(
                        "Uploaded file is not a PDF", status=status.HTTP_400_BAD_REQUEST
                    )

            # return FileResponse(
            #     generated_pdf, as_attachment=True, filename="output.pdf"
            # )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)