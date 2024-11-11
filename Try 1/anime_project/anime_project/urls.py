# anime_project/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import AccueilView  # Importer AccueilView au lieu de la fonction accueil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', AccueilView.as_view(), name='accueil'),  # Utiliser la vue basée sur un template
]