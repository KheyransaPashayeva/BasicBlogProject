from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'phone' , 'project_detail' , 'select' , 'date_submitted')