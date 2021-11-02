from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    file = models.FileField(upload_to='')
    # user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    #user = models.ForeignKey('auth.User',on_delete = models.CASCADE,null=True)
    username = models.ForeignKey(User, blank=True, on_delete = models.CASCADE,null=True)


    def __str__(self):
        return self.title