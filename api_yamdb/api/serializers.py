from rest_framework import serializers

from titles.models import Categories, Genres, Title


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('name', 'slug')


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all()
    )
    categories = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )

    class Meta:
        model = Title
        fields = '__all__'
