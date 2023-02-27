from django.db import models
from users.models import User
from titles.models import Title


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField()
    score = models.IntegerField()
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE
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
        Review, on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )
