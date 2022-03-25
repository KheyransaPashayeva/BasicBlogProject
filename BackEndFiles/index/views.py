from django.shortcuts import render
from .models import NewProject
# Create your views here.
def project(request):
    projects = NewProject.objects.all()
    context = {'project': projects}
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'index.html')


