from django import forms
from django.db import models

from .models import Files

class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('filename','owner','pdf')
        