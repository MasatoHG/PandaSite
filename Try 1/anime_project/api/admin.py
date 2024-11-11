# api/admin.py
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Perso, LiaisonPerso, LiaisonManga, Taille, Poids, Resus, Couleur, Type, Importance, Acteur, Manga, PEGI, Musique, Annee, Mangaka, Editeur


# Enregistrement de tous les modèles
admin.site.register(Perso)
admin.site.register(LiaisonPerso)
admin.site.register(LiaisonManga)
admin.site.register(Taille)
admin.site.register(Poids)
admin.site.register(Resus)
admin.site.register(Couleur)
admin.site.register(Type)
admin.site.register(Importance)
admin.site.register(Acteur)
admin.site.register(Manga)
admin.site.register(PEGI)
admin.site.register(Musique)
admin.site.register(Annee)
admin.site.register(Mangaka)
admin.site.register(Editeur)