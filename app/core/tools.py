from django.core.exceptions import ValidationError
import markdown_checker

def validate_markdown(value):
    if not value.name.endswith(('.md','.markdown')):
        raise ValidationError('File must be markdown file')
    content = value.read().decode('utf-8')
    errors = markdown_checker(content)
    if errors:
        raise ValidationError('Markdown syntax error')