from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)  # Заголовок статьи
    text = models.CharField(max_length=1024)  # Текст статьи
    author = models.CharField(max_length=255)  # Автор статьи

    def __str__(self):
        return self.title
