from django import forms

from .models import Kategoria, Ksiazka, Recenzja


class KsiazkaForm(forms.ModelForm):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'opis', 'okladka', 'kategoria']

    tytul = forms.CharField(label="Tytuł")
    okladka = forms.ImageField(label="Okładka")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kategoria'].queryset = Kategoria.objects.all()
        self.fields['kategoria'].empty_label = "Wybierz kategorię"


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Recenzja
        fields = ['tresc_recenzji', 'ocena']