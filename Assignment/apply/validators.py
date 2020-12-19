from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.conf import settings
import re

def validate_filesize(cv_file):
    # Checks the cv_file for File Size limit. Size limit is 4MB
    if cv_file.size > settings.MAX_FILE_SIZE:
        raise ValidationError('File too large. Size should not exceed 4 MiB.')

def validate_phone_number(phone_number):
    # Validates the input phone number. Only allows local and international format.
    if re.fullmatch(r'^01\d{9}|^\+8801\d{9}', phone_number) is None:
        raise ValidationError("Phone number must be entered in the format: '01XXXXXXXXX' or '+8801XXXXXXXXX'")