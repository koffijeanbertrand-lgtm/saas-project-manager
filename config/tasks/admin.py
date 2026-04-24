from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'project', 'assigned_to', 'created_at']
    list_filter = ['status', 'project']
    search_fields = ['title']
# Register your models here.
