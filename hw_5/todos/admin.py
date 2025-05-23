from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')

