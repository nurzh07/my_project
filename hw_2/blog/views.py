from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()  # Получаем все статьи
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get(id=id)  # Получаем статью по id
    return render(request, 'blog/article_detail.html', {'article': article})
