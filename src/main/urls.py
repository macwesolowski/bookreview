from django.urls import path

from .views import main_view, dodaj_ksiazke_view, ksiazka_detail_view

urlpatterns = [
    path('', main_view, name='main'),
    path('dodaj_ksiazke/', dodaj_ksiazke_view, name='dodaj_ksiazke'),
    path('ksiazka/<uuid:ksiazka_id>/', ksiazka_detail_view, name='ksiazka_detail'),
]