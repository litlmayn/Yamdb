import datetime as dt
from django.db import models
from django.core.validators import MaxValueValidator

from api_yamdb.settings import MAX_LENGHT, SLUG_MAX_LENGHT


class Genres(models.Model):
    name = models.TextField(max_length=MAX_LENGHT)
    slug = models.SlugField(
        'Slug', unique=True,
        max_length=SLUG_MAX_LENGHT
    )
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр произведения'

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.TextField(max_length=MAX_LENGHT)
    slug = models.SlugField(unique=True, max_length=SLUG_MAX_LENGHT)
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория произведения'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'Name', max_length=MAX_LENGHT
    )
    year = models.PositiveSmallIntegerField(
        blank=True, null=True,
        error_messages={'validators': 'Проверьте год'},
        validators=[MaxValueValidator(dt.date.today().year)]
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='сategories',
        blank=True, null=True,
        verbose_name='Категория'
    )
    description = models.TextField(
        'Description', blank=True, null=True,
    )
    genre = models.ManyToManyField(
        Genres,
        blank=True,
        related_name='titles',
        verbose_name='Жанр'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name
