from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()  # Получаем все фильмы
    return render(request, 'movie/movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = Movie.objects.get(id=id)  # Получаем фильм по id
    return render(request, 'movie/movie_detail.html', {'movie': movie})
