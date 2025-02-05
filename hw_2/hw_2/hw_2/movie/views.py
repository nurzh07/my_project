from django.shortcuts import render
from .models import Movie  # Убедитесь, что у вас есть модель Movie

def movie_list(request):
    movies = Movie.objects.all()  # Получаем список фильмов
    return render(request, 'movies/movie_list.html', {'movies': movies})

