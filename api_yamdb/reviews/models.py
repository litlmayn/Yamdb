from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from titles.models import Title
from users.models import User


class Abstraction(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField(
        verbose_name='Текст',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.text


class Review(Abstraction):
    score = models.PositiveSmallIntegerField(
        default=5,
        validators=[
            MinValueValidator(
                1,
                message='Введите оценку от 1 до 10!'
            ),
            MaxValueValidator(
                10,
                message='Введите оценку от 1 до 10!'
            ),
        ],
        verbose_name='Оценка произведения',
    )

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Рецензия которому пишется отзыв',
    )

    class Meta(Abstraction.Meta):
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            ),
        )
        verbose_name_plural = 'Отзывы',
        default_related_name = 'reviews'


class Comment(Abstraction):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв которому пишется комментарий',
    )

    class Meta(Abstraction.Meta):
        verbose_name_plural = 'Комментарии',
        default_related_name = 'comments'
