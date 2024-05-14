from django.db import models

from backend.constants import MAX_LENGTH_CHAR_FIELD, MIN_RATING


class Comment(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR_FIELD, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Review(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR_FIELD)
    text = models.TextField()
    rating = models.IntegerField(default=MIN_RATING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name