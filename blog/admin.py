from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Показываем эти поля в списке
    search_fields = ('title', 'content')  # Возможность поиска по этим полям
    list_filter = ('author', 'created_at')  # Фильтрация по этим полям

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')  # Показываем эти поля в списке
    search_fields = ('text',)
    list_filter = ('author', 'created_at')  # Фильтрация по этим полям
