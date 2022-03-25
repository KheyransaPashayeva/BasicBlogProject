from django.db import models
from distutils.command.upload import upload
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=170)
    date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=270)
    image = models.ImageField(upload_to='blogposts/',null=True, blank=True)
    text = models.TextField()
    agency = models.IntegerField()
    project_detail = models.TextField()
    
    def __str__(self):
        return self.title