from django.contrib import admin
from django.conf import settings

from titles.models import Categories, Genres, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'year',
        'description', 'category',
    )
    search_fields = ('name', 'year')
    list_filter = ('name',)
    list_editable = (
        'name', 'year',
        'description', 'category',
    )
    empty_value_display = settings.VALUE_DISPLAY

    def get_genre(self, object):
        return ', '.join((genre.name for genre in object.genre.all()))


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'description',)
    search_fields = ('name', 'slug', 'description',)
    list_filter = ('name',)
    list_editable = ('name', 'slug', 'description',)
    empty_value_display = settings.VALUE_DISPLAY


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'description',)
    search_fields = ('name', 'slug', 'description',)
    list_filter = ('name',)
    list_editable = ('name', 'slug', 'description',)
    empty_value_display = settings.VALUE_DISPLAY
