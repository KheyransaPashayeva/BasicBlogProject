from django.shortcuts import render
from .models import Project

def allproject(request):
    allprojects = Project.objects.all()
    context = {'project': allprojects}
    return render(request, 'single-project.html', context)

def project(request):
    return render(request, 'single-project.html')