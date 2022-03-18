from django.db import models
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=127)
    phone = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    select = models.CharField(null=True,blank=True,max_length=70)
    project_detail = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.email