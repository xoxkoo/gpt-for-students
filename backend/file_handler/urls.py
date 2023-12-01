from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    # Define more URL patterns for other endpoints if needed
]
