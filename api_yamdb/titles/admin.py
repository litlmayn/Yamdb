from django.contrib import admin

from api_yamdb.settings import VALUE_DISPLAY
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
    empty_value_display = VALUE_DISPLAY


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'description',)
    search_fields = ('name', 'slug', 'description',)
    list_filter = ('name',)
    list_editable = ('name', 'slug', 'description',)
    empty_value_display = VALUE_DISPLAY


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'description',)
    search_fields = ('name', 'slug', 'description',)
    list_filter = ('name',)
    list_editable = ('name', 'slug', 'description',)
    empty_value_display = VALUE_DISPLAY
