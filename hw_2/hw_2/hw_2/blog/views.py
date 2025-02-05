from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Article

# Получение списка всех статей
def article_list(request):
    articles = list(Article.objects.values())  # Преобразуем QuerySet в список
    return JsonResponse(articles, safe=False)

# Получение информации о конкретной статье
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return JsonResponse({
        "id": article.id,
        "title": article.title,
        "text": article.text,
        "author": article.author,
    })

