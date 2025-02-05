from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list, name='article_list'),  # Список статей
    path('articles/<int:id>/', article_detail, name='article_detail'),  # Детали статьи
]
