from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)  # Название фильма
    description = models.CharField(max_length=255)  # Описание фильма
    producer = models.CharField(max_length=255)  # Производитель
    duration = models.IntegerField()  # Продолжительность фильма в секундах

    def __str__(self):
        return self.title
