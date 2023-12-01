from django.apps import AppConfig

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

def upload(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']

        # Ensure the uploaded file is a PDF
        if pdf_file.name.endswith('.pdf'):
            # Create a directory to save uploaded files if it doesn't exist
            upload_dir = 'uploaded_pdfs'
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            # Save the uploaded PDF file to the server
            with open(os.path.join(upload_dir, pdf_file.name), 'wb') as destination:
                for chunk in pdf_file.chunks():
                    destination.write(chunk)

            return JsonResponse({'message': 'PDF file uploaded successfully'})
        else:
            return JsonResponse({'error': 'Uploaded file is not a PDF'}, status=400)
    else:
        return JsonResponse({'error': 'No PDF file uploaded or invalid request'}, status=400)
