from django.shortcuts import render
from .models import AllComment

def post(request):
    if request.method == 'POST':
        comment = AllComment()
        name=request.POST.get('name')
        email=request.POST.get('email')
        your_comment=request.POST.get('your_comment')
        comment.name=name
        comment.email=email
        comment.your_comment=your_comment
        comment.save()
        return render(request, 'single-post.html')
   
    return render(request, 'single-post.html')
