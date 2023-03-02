from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from titles.models import Title
from users.models import User


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField()
    score = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                1,
                message='Введите оценку от 1 до 10!'
            ),
            MaxValueValidator(
                10,
                message='Введите оценку от 1 до 10!'
            ),
        ]
    )

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            ),
        )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField()
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    def __str__(self):
        return self.text
