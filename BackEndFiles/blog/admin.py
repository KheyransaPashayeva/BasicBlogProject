from django.contrib import admin
from .models import NewBlogPost
# Register your models here.
@admin.register(NewBlogPost)
class NewBlogPostAdmin(admin.ModelAdmin):
    list_display = ('author' , 'title')