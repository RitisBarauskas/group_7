from django.db import models

from backend.constants import MIN_RATING, MAX_LENGTH_CHAR_FIELD


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