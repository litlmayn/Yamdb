from api.views import SignupViewSet, UserViewSet, TokenViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenViewSet),
    path('auth/signup', SignupViewSet),
]
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
