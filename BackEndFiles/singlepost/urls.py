from django.urls import path
from singlepost.views import post


app_name='singlepost'
urlpatterns = [
    path('', post, name='post')
]