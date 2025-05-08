from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('threads/', views.threads_list, name='threads_list'),
    path('threads/create/', views.create_thread, name='create_thread'),
    path('threads/<int:id>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:id>/delete/', views.delete_thread, name='delete_thread'),
    path('threads/<int:id>/edit/', views.edit_thread, name='edit_thread'),
    path('threads/<int:thread_id>/posts/create/', views.create_post, name='create_post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit_post'),
]
