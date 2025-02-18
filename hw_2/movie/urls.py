from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Список фильмов
    path('<int:id>/', views.movie_detail, name='movie_detail'),  # Детали фильма
]
