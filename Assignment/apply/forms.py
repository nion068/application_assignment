from django import forms
from django.core.validators import validate_email, FileExtensionValidator
from .validators import validate_filesize, validate_phone_number
from django.conf import settings

class AuthenticationForm(forms.Form):
    # This form is used in login.html page. Takes input username and password.
    user_name = forms.CharField(strip=True)
    password = forms.CharField(widget=forms.PasswordInput)

class DetailsForm(forms.Form):
    # This form is used in details.html page. 
    # Takes all the necessary inputs specified in the assignment description.
    # Handles specified restrictions. Custom validators are written in validators.py
    name = forms.CharField(max_length=256, strip=True)
    email = forms.EmailField(max_length=256, widget=forms.EmailInput, validators=[validate_email])
    phone = forms.CharField(max_length=14, validators=[validate_phone_number])
    full_address = forms.CharField(max_length=512)
    name_of_university = forms.CharField(max_length=256)
    graduation_year = forms.IntegerField(max_value=2020, min_value=2015)
    cgpa = forms.FloatField(max_value=4.0, min_value=2.0, required=False)
    experience_in_months = forms.IntegerField(max_value=100, min_value=0, required=False)
    current_work_place_name = forms.CharField(max_length=256, required=False)
    applying_in = forms.ChoiceField(choices=settings.APPLY_CHOICES)
    expected_salary = forms.IntegerField(max_value=60000, min_value=15000)
    field_buzz_reference = forms.CharField(max_length=256, required=False)
    github_project_url = forms.URLField(max_length=512)
    cv_file = forms.FileField(widget=forms.FileInput, allow_empty_file=False, validators=[FileExtensionValidator(allowed_extensions=['pdf']), validate_filesize])