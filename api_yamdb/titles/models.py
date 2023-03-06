from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from .validators import year_validator


class GenresCategories(models.Model):
    name = models.TextField(max_length=settings.MAX_LENGHT)
    slug = models.SlugField(
        'Slug', unique=True,
        max_length=settings.SLUG_MAX_LENGHT
    )
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        abstract = True

    def __str__(self):
        return self.name


class Genres(GenresCategories):

    class Meta(GenresCategories.Meta):
        verbose_name = 'Жанр произведения'


class Categories(GenresCategories):

    class Meta(GenresCategories.Meta):
        verbose_name = 'Категория произведения'


class Title(models.Model):
    name = models.CharField(
        'Name', max_length=settings.MAX_LENGHT
    )
    year = models.PositiveSmallIntegerField(
        blank=True, null=True,
        error_messages={'validators': 'Проверьте год'},
        validators=[
            MinValueValidator(0,),
            year_validator
        ],
        db_index=True
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
