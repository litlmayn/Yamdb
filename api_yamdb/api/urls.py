from api.views import (SignupViewSet, UserViewSet,
                       TokenViewSet, CategoriesViewSet,
                       TitlesViewSet, GenresViewSet,
                       ReviewViewset, CommentViewSet)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
router.register(
    r'titles', TitlesViewSet, basename='titles'
)
router.register(
    r'categories', CategoriesViewSet, basename='categories'
)
router.register(
    r'genres', GenresViewSet, basename='genres'
)
router.register(
    r'reviews', ReviewViewset, basename='reviews'
)
router.register(
    r'comments', CommentViewSet, basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', TokenViewSet),
    path('v1/auth/signup/', SignupViewSet),
]
