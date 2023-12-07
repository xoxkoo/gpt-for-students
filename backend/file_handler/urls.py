from django.urls import path
from .views import FileUploadView

urlpatterns = [
    path("file_handler/", FileUploadView.as_view(), name="file_handler"),
    # Define more URL patterns for other endpoints if needed
]
