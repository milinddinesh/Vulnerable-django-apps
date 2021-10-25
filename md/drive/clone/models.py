from django.db import models

# Create your models here.
# class FilesUpload(models.Model):
    # file = models.FileField()

class Files(models.Model):
    filename = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')