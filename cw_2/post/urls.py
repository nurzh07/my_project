from django.urls import path
from .views import get_posts, get_post, create_post, delete_post

urlpatterns = [
    path('posts/', get_posts, name='get_posts'),
    path('posts/<int:post_id>/', get_post, name='get_post'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
]
