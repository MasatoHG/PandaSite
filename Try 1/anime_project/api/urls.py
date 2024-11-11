# api/urls.py
from django.urls import path
from . import views
from .views import PersoListView

urlpatterns = [
    path("personnages/", PersoListView.as_view(), name="personnages_list"),  # API JSON
    path('personnages/html/', views.PersoListTemplateView.as_view(), name='personnages_list_html'),  # Vue HTML
]