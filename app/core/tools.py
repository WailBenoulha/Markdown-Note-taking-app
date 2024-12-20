from django.core.exceptions import ValidationError
import markdown_checker

def validate_markdown(value):
    content = value.read().decode('utf-8')
    errors = markdown_checker(content)
    if errors:
        raise ValidationError('Markdown syntax error')