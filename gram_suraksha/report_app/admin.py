from django.contrib import admin
from .models import Issue, StatusUpdate

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('category', 'user__username')

@admin.register(StatusUpdate)
class StatusUpdateAdmin(admin.ModelAdmin):
    list_display = ('issue', 'status', 'updated_at')
