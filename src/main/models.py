from django.contrib.auth.models import User

import uuid

from django.db import models
from .utils import book_cover_upload_path
from .consts import GENRES


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=30, choices=GENRES, default=None)

    def __str__(self):
        return self.nazwa


class Ksiazka(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    tytul = models.CharField(max_length=140)
    autor = models.CharField(max_length=140)
    opis = models.TextField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    okladka = models.ImageField(upload_to=book_cover_upload_path, blank=True, null=True)

    def average_rating(self):
        recenzje = self.recenzje.all()
        if recenzje.exists():
            return round(sum(r.ocena for r in recenzje) / recenzje.count(), 1)
        return 0

    def __str__(self):
        return self.tytul


class Recenzja(models.Model):
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, related_name="recenzje")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tresc_recenzji = models.TextField()
    ocena = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])  # Ocena 1-5 gwiazdek
    data_dodania = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('ksiazka', 'autor')  # Każdy użytkownik może dodać tylko jedną recenzję danej książki
        ordering = ['-data_dodania']  # Najnowsze recenzje pierwsze

    def __str__(self):
        return f'Recenzja {self.ksiazka.tytul} przez {self.autor.username}'


