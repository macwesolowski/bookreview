import django_filters

from .models import Ksiazka, Kategoria


class KategoriaFilter(django_filters.FilterSet):

    class Meta:
        model = Kategoria
        fields = {'nazwa': {'exact'}}


class KsiazkaFilter(django_filters.FilterSet):

    class Meta:
        model = Ksiazka
        fields = {'kategoria': {'exact'}, 'tytul': {'icontains'}, 'autor': {'icontains'}}