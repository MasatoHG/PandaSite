# api/views.py
from django.views.generic import ListView
from rest_framework import generics
from .models import Perso  # Import du modèle Perso
from .serializers import PersoSerializer

# Vue API pour lister les personnages (format JSON avec Django REST Framework)
class PersoListView(ListView):
    model = Perso
    template_name = "personnages_list.html"
    context_object_name = "personnages"

# Vue HTML pour lister les personnages dans un template
class PersoListTemplateView(ListView):
    model = Perso
    template_name = 'api/personnages_list.html'  # Emplacement du template HTML
    context_object_name = 'personnages'
    # api/views.py

# api/views.py
from django.views.generic import TemplateView

# Vue pour afficher la page d'accueil avec un template
class AccueilView(TemplateView):
    template_name = "accueil.html"