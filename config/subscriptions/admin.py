from django.contrib import admin
from .models import Plan, Subscription


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'max_organizations', 'max_projects', 'max_tasks', 'is_active']
    list_editable = ['price', 'max_organizations', 'max_projects', 'max_tasks', 'is_active']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'status', 'started_at', 'expires_at']
    list_filter = ['status', 'plan']

# Register your models here.
