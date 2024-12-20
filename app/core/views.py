from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import request,status
from rest_framework.response import Response
from .models import Note
from .serializers import UploadMarkdown
from rest_framework.parsers import MultiPartParser,FileUploadParser


class UploadView(APIView):
    serializer_class = UploadMarkdown
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser,FileUploadParser)

    def post(self,request):
        serializers = UploadMarkdown(data=request.data)
        if serializers.is_valid():
            if serializers.validated_data['note'].name.endswith(('.md','.markdown')):
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response({'error':'the file form should be .md'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ListNotes(APIView):
    serializer_class = UploadMarkdown
    permission_classes = [AllowAny]    

    def get(self,request):
        model = Note.objects.all()
        serializer = UploadMarkdown(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
# class CheckGrammer(APIView):
#     serializer_class = UploadMarkdown
#     permission_classes = [AllowAny]    

#     def post(self,request):