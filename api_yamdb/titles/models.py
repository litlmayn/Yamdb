from django.db import models


class Genres(models.Model):
    name = models.TextField(max_length=50)
    slug = models.SlugField(
        'Slug', unique=True
    )
    description = models.TextField()


class Categories(models.Model):
    name = models.TextField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()


class Title(models.Model):
    name = models.TextField()
    year = models.IntegerField(
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genres,
    )
    categories = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='сategories',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
