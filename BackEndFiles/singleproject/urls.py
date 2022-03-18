from django.urls import path
from singleproject.views import project


app_name='singleproject'
urlpatterns = [
    path('', project, name='project')
]