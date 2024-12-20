from django.urls import path
from .views import UploadView,ListNotes,CheckGrammer,MarkdownToHTML

urlpatterns = [
    path('upload/',UploadView.as_view(),name='upload'),
    path('notes/',ListNotes.as_view(),name='notes'),
    path('check-gram/',CheckGrammer.as_view(),name='check'),
    path('html/',MarkdownToHTML.as_view(),name='html')
]