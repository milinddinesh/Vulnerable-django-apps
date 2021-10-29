from django import forms
from .models import Document

class UploadFileForm(forms.Form):
    class Meta:
        model = Document
        field = forms.FileField()
        