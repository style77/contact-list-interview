def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xls', '.xlsx', '.csv']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension.')
