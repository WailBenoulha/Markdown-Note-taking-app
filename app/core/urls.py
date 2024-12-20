from django.urls import path
from .views import UploadView,ListNotes

urlpatterns = [
    path('upload/',UploadView.as_view(),name='upload'),
    path('notes/',ListNotes.as_view(),name='notes')
]