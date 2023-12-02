import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt  # idk what is this
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('summarize_file'):
        file = request.FILES['summarize_file']

        # now we save only a PDF
        if file.name.endswith('.pdf'):
            # Create a directory to save uploaded files if it doesn't exist
            upload_dir = 'files'
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            # Save the uploaded PDF file to the server
            file_id = unique_file_name(file.name)
            with open(os.path.join(upload_dir, file_id), 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            print('PDF file uploaded successfully')
            return JsonResponse({'message': 'PDF file uploaded successfully', 'file_id': file_id})
        else:
            return JsonResponse({'error': 'Uploaded file is not a PDF'}, status=400)
    else:
        return JsonResponse({'error': 'No PDF file uploaded or invalid request'}, status=400)

def unique_file_name(name):
    file_extension = os.path.splitext(name)[1] if '.' in name else ''
    generated_uuid = str(uuid.uuid4())
    unique_name = generated_uuid + file_extension
    return unique_name