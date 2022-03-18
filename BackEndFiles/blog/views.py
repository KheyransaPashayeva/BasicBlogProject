from django.shortcuts import render
from .models import NewBlogPost
# Create your views here.
def blog(request):
    posts = NewBlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'blog.html', context)