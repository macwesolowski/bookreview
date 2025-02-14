from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.http import JsonResponse
from django.db.models import Avg

from .forms import KsiazkaForm, AddReviewForm
from .models import Ksiazka
from .filters import KsiazkaFilter

from django.core.paginator import Paginator

import os
from django.conf import settings
import random


def losowy_cytat():
    file_path = os.path.join(settings.BASE_DIR, "main\data\cytaty.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # Wybieramy losowy cytat
            losowy_wiersz = random.choice(lines).strip()

            # Rozdzielamy autora i cytat
            autor, cytat = losowy_wiersz.split("|", 1)

            return autor.strip(), cytat.strip()

    except (FileNotFoundError, ValueError):
        return "Brak autora", "Brak cytatu"


def main_view(request):
    listings = Ksiazka.objects.all()
    listing_filter = KsiazkaFilter(request.GET, queryset=listings)

    paginator = Paginator(listing_filter.qs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    autor, cytat = losowy_cytat()

    context = {
        'listings': listings,
        'listing_filter': listing_filter,
        'page_obj': page_obj,
        'cytat': cytat,
        'autor': autor
    }
    return render(request, 'views/main.html', context)


def dodaj_ksiazke_view(request):
    # Jeśli użytkownik nie jest zalogowany, przekierowujemy go bez parametru next
    if not request.user.is_authenticated:
        return redirect('main')  # lub jakakolwiek inna strona główna

    # Jeśli użytkownik nie jest superużytkownikiem, przekierowujemy na stronę główną
    if not request.user.is_superuser:
        return redirect('main')

    if request.method == "POST":
        form = KsiazkaForm(request.POST, request.FILES)
        form.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, "Książka została dodana!")
            form = KsiazkaForm()
    else:
        form = KsiazkaForm()

    return render(request, 'views/dodaj_ksiazke.html', {'form': form})


def ksiazka_detail_view(request, ksiazka_id):
    ksiazka = get_object_or_404(Ksiazka, id=ksiazka_id)
    srednia_ocena = ksiazka.recenzje.aggregate(Avg('ocena'))['ocena__avg'] or 0
    form = AddReviewForm() if request.user.is_authenticated else None

    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        if not request.user.is_authenticated:
            return JsonResponse({"success": False, "message": "Musisz być zalogowany, aby dodać recenzję."}, status=403)

        form = AddReviewForm(request.POST)
        if form.is_valid():
            recenzja = form.save(commit=False)
            recenzja.ksiazka = ksiazka
            recenzja.autor = request.user
            recenzja.save()

            nowa_srednia = ksiazka.recenzje.aggregate(Avg('ocena'))['ocena__avg'] or 0

            return JsonResponse({
                "success": True,
                "srednia_ocena": round(nowa_srednia, 2),
                "autor": request.user.username,
                "ocena": recenzja.ocena,
                "tresc_recenzji": recenzja.tresc_recenzji
            })

        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    context = {
        'ksiazka': ksiazka,
        'srednia_ocena': round(srednia_ocena, 2),
        'form': form,
        'oceny': range(1, 6)
    }

    return render(request, 'views/ksiazka_detail.html', context)