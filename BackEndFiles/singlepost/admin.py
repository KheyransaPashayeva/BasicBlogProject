from django.contrib import admin
from .models import AllComment

@admin.register(AllComment)
class AllCommentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'your_comment' , 'date_submitted')