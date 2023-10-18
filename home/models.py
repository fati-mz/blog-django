from django.db import models
from datetime import datetime    

class Contact(models.Model):
    name= models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name