from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CategoriesViewSet, TitlesViewSet, GenresViewSet
from review.views import ReviewViewset, CommentViewSet

router = SimpleRouter()
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
    r'titles', ReviewViewset, basename='reviews'
)
router.register(
    r'titles', CommentViewSet, basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
]
