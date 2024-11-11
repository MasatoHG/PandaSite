# api/serializers.py
from rest_framework import serializers
from .models import Perso

class PersoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perso
        fields = '__all__'  # Inclure tous les champs du modèle