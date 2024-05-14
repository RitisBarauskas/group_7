from django.db import models

from backend.constants import MAX_LENGTH_CHAR_FIELD


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
