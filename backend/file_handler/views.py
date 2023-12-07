import uuid
import os
import pickle
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from django.core.files.base import ContentFile


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file = serializer.validated_data["file"]
            # Get the name without extension
            file_name = os.path.splitext(uploaded_file.name)[0]
            # Get the extension
            file_extension = os.path.splitext(uploaded_file.name)[1][1:]
            # Check if 'title' parameter is present and has a value
            if (
                "title" in serializer.validated_data
                and serializer.validated_data["title"]
            ):
                # 'title' is present and has a value, do nothing
                pass
            else:
                # 'title' is not present or has no value, set it to 'file_name'
                serializer.validated_data["title"] = file_name

            # split pdf into text chunks
            if uploaded_file is not None and file_extension.lower() == "pdf":
                pdf_reader = PdfReader(uploaded_file)

                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000, chunk_overlap=200, length_function=len
                )
                chunks = text_splitter.split_text(text=text)

                # transform pdf into pkl with embeddings
                store_name = str(uuid.uuid4())

                embeddings = OpenAIEmbeddings()
                VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
                pkl_filename = f"{store_name}.pkl"

                # Save the PKL data to the new file
                with open(f"{store_name}.pkl", "wb") as f:
                    serialized_data = VectorStore.serialize_to_bytes()
                    f.write(serialized_data)

                # Update the serializer's file field to use the new PKL file
                with open(f"{store_name}.pkl", "rb") as pkl_file:
                    serializer.validated_data["file"] = ContentFile(
                        pkl_file.read(), name=f"{store_name}.pkl"
                    )

                # Save the serializer
                serializer.save()

                # Clean up: Remove the temporary PKL file
                os.remove(pkl_filename)
            else:
                return Response(
                    "Uploaded file is not a PDF", status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {"recreated_pdf": f"{pkl_filename} saved"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def unique_file_name(name):
    file_extension = os.path.splitext(name)[1] if "." in name else ""
    generated_uuid = str(uuid.uuid4())
    unique_name = generated_uuid + file_extension
    return unique_name
