from rest_framework import serializers
from rest_framework.serializers import FileField
from.models import Note,SubNote

class UploadMarkdown(serializers.ModelSerializer):
    note = FileField()
    class Meta:
        model = Note
        fields = ['id','title','note'] 

class SubNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubNote
        fields = '__all__'          