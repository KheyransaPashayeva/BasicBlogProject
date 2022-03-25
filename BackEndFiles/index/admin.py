from django.contrib import admin
from .models import NewProject

@admin.register(NewProject)
class NewProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')