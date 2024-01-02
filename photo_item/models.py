from django.db import models
from django.contrib.auth.models import User

class PhotoItem(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField() 
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name