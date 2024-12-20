from django.db import models
from .tools import validate_markdown
from django.core.exceptions import ValidationError
import markdown_checker

class Note(models.Model):
    title = models.CharField(max_length=255)
    note = models.FileField(upload_to='file',validators=[validate_markdown])

    def __str__(self):
        return self.title
    

class SubNote(models.Model):
    note = models.ForeignKey(Note,on_delete=models.CASCADE,related_name='subnote')    