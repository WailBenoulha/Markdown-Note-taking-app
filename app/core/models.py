from django.db import models
from .tools import validate_markdown
from django.core.exceptions import ValidationError
import markdown_checker

class Note(models.Model):
    title = models.CharField(max_length=255)
    note = models.FileField(upload_to='file',validators=[validate_markdown])

    def __str__(self):
        return self.title
    
    # def save(self,*args,**kwargs):
    #     if not self.note.name.endswith(('.md','.markdown')):
    #         raise ValidationError('File must be a markdown file')
    #     super().save(*args, **kwargs)