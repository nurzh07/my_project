from django.urls import path
from . import views  # Убеждаемся, что импортируем views из текущего приложения

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('new/', views.post_create, name='post_create'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
    path('<int:id>/delete/', views.post_delete, name='post_delete'),
]