from django.contrib import admin

from .models import Kategoria, Ksiazka, Recenzja


class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('nazwa',)
    ordering = ('nazwa',)


class KsiazkaAdmin(admin.ModelAdmin):
    pass


class RecenzjaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(Ksiazka, KsiazkaAdmin)
admin.site.register(Recenzja, RecenzjaAdmin)

