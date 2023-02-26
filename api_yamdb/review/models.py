from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
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
    text = models.TextField()
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )
