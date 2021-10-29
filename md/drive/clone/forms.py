from django import forms
from django.db import models

# from .models import Files_Upload

class FileForm(forms.ModelForm):
    file = forms.FileField()
        