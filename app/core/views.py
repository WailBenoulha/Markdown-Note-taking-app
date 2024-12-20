from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import request,status
from rest_framework.response import Response
from .models import Note,SubNote
from .serializers import UploadMarkdown,SubNoteSerializer
from rest_framework.parsers import MultiPartParser,FileUploadParser
from markdown_checker import check_url

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
    
import language_tool_python
# this library is for checking grammar of the text
# here we check the grammar of the note field (its a foreign key of Note class)

class CheckGrammer(APIView):
    serializer_class = SubNoteSerializer
    permission_classes = [AllowAny]    

    def post(self,request):
        serializer = SubNoteSerializer(data=request.data)
        if serializer.is_valid():
            note_id = serializer.validated_data['note'].id
            note_instance = Note.objects.get(id=note_id)
            file_path = note_instance.note.path
            with open(file_path,'r') as f:
                text = f.read()
            tool = language_tool_python.LanguageTool('en-US')
            result = tool.check(text)
            organized_result = []
            for match in result:
                organized_result.append({
                    'message': match.message,
                    'suggestions': match.replacements,
                    'offset': match.offset,
                    'length': match.errorLength,
                    'context': match.context,
                })
            return Response({'result':organized_result},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
import markdown

class MarkdownToHTML(APIView):
    serializer_class = SubNoteSerializer    
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = SubNoteSerializer(data=request.data)
        if serializer.is_valid():
            note_id = serializer.validated_data['note'].id
            note_instance = Note.objects.get(id=note_id)
            file_path = note_instance.note.path
            with open(file_path,'r') as f:
                text = f.read()
            result = markdown.markdown(text) 
            return Response(result,status=status.HTTP_201_CREATED)   
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)