from django.urls import path
from .views import FileQueryView

urlpatterns = [
    path("chatter/", FileQueryView.as_view(), name="chatter"),
    # Define more URL patterns for other endpoints if needed
]
