from django.urls import path
from .views import FileSummarizeView

urlpatterns = [
    path("summarizer/", FileSummarizeView.as_view(), name="summarizer"),
    # Define more URL patterns for other endpoints if needed
]
