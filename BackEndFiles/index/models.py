from django.db import models
from distutils.command.upload import upload
# Create your models here.
class NewProject(models.Model):
    name = models.CharField(max_length=127)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogposts/',null=True, blank=True)