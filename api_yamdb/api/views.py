from rest_framework import viewsets, mixins

from .serializers import GenresSerializer, TitleSerializer, CategorieSerializer
from titles.models import Title, Genres, Categories


class GetListCreateDeleteViewSet(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 mixins.DestroyModelMixin,
                                 viewsets.GenericViewSet):
    pass


class GenresViewSet(GetListCreateDeleteViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class CategoriesViewSet(GetListCreateDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorieSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

