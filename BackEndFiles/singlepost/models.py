from django.db import models
from django.utils import timezone
# Create your models here.

class AllComment(models.Model):
    name = models.CharField(max_length=127)
    email = models.EmailField(max_length=70)
    your_comment = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name