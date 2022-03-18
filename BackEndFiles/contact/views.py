from django.shortcuts import render
from .models import Message

def contact(request):
    if request.method == 'POST':
        contact = Message()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        select=request.POST.get('select')
        project_detail=request.POST.get('project_detail')
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.select=select
        contact.project_detail=project_detail
        contact.save()
        return render(request, 'index.html')
   
    return render(request, 'contact.html')
# Create your views here.

