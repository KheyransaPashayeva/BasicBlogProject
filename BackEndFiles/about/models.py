from django.db import models
from django.utils import timezone

class About(models.Model):
    body = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.body