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
    name = models.CharField(
        'Name', max_length=200
    )
    year = models.IntegerField(
        blank=True, null=True
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='сategories',
        blank=True, null=True,
    )
    rating = models.IntegerField(
        blank=True, null=True,
    )
    description = models.TextField(
        'Description', blank=True, null=True,
    )
    genre = models.ManyToManyField(
        Genres,
        blank=True,
        related_name='titles',
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
