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
