from api.validators import username_validator
from django.db.models import Avg
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
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating',
            'description', 'genre', 'category',
        )
        filter_backends = (filters.SearchFilter,)
        search_fields = ('genre')

    def get_rating(self, obj):
        return obj.reviews.all().aggregate(Avg('score'))['score__avg']


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
