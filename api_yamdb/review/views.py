from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)

from ..api_yamdb.serializers import CommentSerializer, ReviewSerializer
from .models import Title, Comment, Review
from ..api_yamdb.permissions import IsAuthorOrReadOnly

class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_title(self):
        """Достаем произведение."""
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        """Проверка отзыва."""
        return Review.objects.filter(title_id=self.get_title().id)

    def perform_create(self, serializer):
        """Создание отзыва."""
        serializer.save(
            author=self.request.user,
            title=self.get_title()
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_review(self):
        """Достаем отзыв."""
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def get_queryset(self):
        """Проверка комментария."""
        return Comment.objects.filter(review_id=self.get_review().id)

    def perform_create(self, serializer):
        """Создание комментария."""
        serializer.save(
            author=self.request.user,
            title=self.get_review()
        )
