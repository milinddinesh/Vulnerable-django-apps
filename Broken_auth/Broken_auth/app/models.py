from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='media/')     

    def __str__(self):
        return self.title