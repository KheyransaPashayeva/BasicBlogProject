from django.db import models
from distutils.command.upload import upload
# Create your models here.
class NewBlogPost(models.Model):
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=70)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogposts/',null=True, blank=True)
    text = models.TextField()
    author_img = models.ImageField(upload_to='blogposts/',null=True)
    comment_say = models.IntegerField(max_length=100000)

    def __str__(self):
        return self.author