from api.validators import username_validator
import datetime as dt
from rest_framework import serializers, filters

from reviews.models import Review, Comment
from titles.models import Categories, Genres, Title
from users.models import User
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z', max_length=settings.MAX_LENGHT_USERNAME,
        validators=(username_validator,))

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True}}

    def validate_username(self, value):
        return username_validator(value)


class ProfileSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        read_only_fields = ('role',)


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z', max_length=settings.MAX_LENGHT_USERNAME,
        validators=(username_validator,))
    email = serializers.EmailField(max_length=settings.MAX_LENGHT_EMAIL)

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        return username_validator(value)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=settings.MAX_LENGHT_USERNAME, required=True)
    confirmation_code = serializers.CharField(
        max_length=settings.MAX_LENGHT_EMAIL, required=True)

    class Meta:
        model = User
        fields = (
            'username', 'confirmation_code')

    def validate_username(self, value):
        return username_validator(value)


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('name', 'slug')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name', 'slug')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GenresSerializer(value)
        return serializer.data


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorieSerializer(value)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True
    )
    category = CategoryField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year',
            'description', 'genre', 'category',
        )
        filter_backends = (filters.SearchFilter,)
        search_fields = ('genre')

    def validate_year(self, value):
        kw_data = self._kwargs['data']
        category = kw_data['category']
        if category == 'movie':
            year = dt.date.today().year
            start_year = 1895
            error_msg = 'Проверьте год создания произведения!'
            if not (start_year < value <= year):
                raise serializers.ValidationError(error_msg)
        return value


class ReadTitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(read_only=True)
    genre = GenresSerializer(read_only=True, many=True)
    category = CategorieSerializer(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'description',
            'genre', 'category', 'rating',
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True,
    )

    class Meta:
        model = Review
        fields = (
            'id', 'text', 'author', 'score', 'pub_date',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = (
            'id', 'text', 'author', 'pub_date',
        )
