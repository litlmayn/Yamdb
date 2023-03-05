from django.db import IntegrityError
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .mixins import GetListCreateDeleteViewSet
from .permissions import (
    IsAdminOrReadOnly, IsAdminOrSuperUser, IsUserAdminModeratorOrReadOnly
)
from .serializers import (
    SignupSerializer, UserSerializer, ProfileSerializer, TokenSerializer,
    GenresSerializer, TitleSerializer, CategorieSerializer, CommentSerializer,
    ReviewSerializer, ReadTitleSerializer)
from .filters import TitleFilter
from reviews.models import Review
from titles.models import Title, Genres, Categories
from users.models import User


class GenresViewSet(GetListCreateDeleteViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class CategoriesViewSet(GetListCreateDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorieSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = TitleFilter
    ordering_fields = ('year', 'name', 'category')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TitleSerializer
        return ReadTitleSerializer


@api_view(['POST'])
def signup(request):
    EMAIL_ERROR = 'Электронная почта уже занята!'
    USERNAME_ERROR = 'Имя пользователя уже занято!'
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    try:
        user, _ = User.objects.get_or_create(
            username=username, email=email)
    except IntegrityError:
        error = (
            EMAIL_ERROR if User.objects.filter(email=email).exists()
            else USERNAME_ERROR)
        return Response(
            error, status=status.HTTP_400_BAD_REQUEST)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Код подтверждения',
        f'Ваш код подтверждения: {confirmation_code}',
        f'{settings.EMAIL_YAMDB}',
        [email],
        fail_silently=False,)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    confirmation_code = serializer.validated_data.get('confirmation_code')
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, confirmation_code):
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response(
        {'confirmation_code': 'Неверный код подтверждения'},
        status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete')
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrSuperUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'
    lookup_value_regex = r'[\w\@\.\+\-]+'

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path='me',
    )
    def get_profile(self, request):
        if request.method == 'PATCH':
            serializer = ProfileSerializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsUserAdminModeratorOrReadOnly]
    pagination_class = PageNumberPagination

    def get_title(self):
        """Достаем произведение."""
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        """Проверка отзыва."""
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
        """Создание отзыва."""
        serializer.save(
            author=self.request.user,
            title=self.get_title(),
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsUserAdminModeratorOrReadOnly,
    )
    pagination_class = PageNumberPagination

    def get_review(self):
        """Достаем отзыв."""
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def get_queryset(self):
        """Проверка комментария."""
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        """Создание комментария."""
        serializer.save(
            author=self.request.user,
            review=self.get_review()
        )
