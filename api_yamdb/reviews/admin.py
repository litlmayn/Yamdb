from django.contrib import admin

from .models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'author', 'pub_date',
        'text', 'score', 'title',
    )
    search_fields = 'author'
    list_filter = 'pub_date'
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'author', 'pub_date',
        'text', 'review',
    )
    search_fields = 'author'
    list_filter = 'pub_date'
    empty_value_display = '-пусто-'


admin.site.register(Comment)
admin.site.register(Review)
