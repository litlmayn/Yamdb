from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (signup, UserViewSet,
                       get_token, CategoriesViewSet,
                       TitlesViewSet, GenresViewSet,
                       ReviewViewset, CommentViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

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
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewset, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

auth = [
    path('token/', get_token, name='token'),
    path('signup/', signup, name='signup')
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth))
]
