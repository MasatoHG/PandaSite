# api/models.py
from django.db import models

class Taille(models.Model):
    cm = models.IntegerField()

    def __str__(self):
        return f"{self.cm} cm"


class Poids(models.Model):
    kg = models.FloatField()

    def __str__(self):
        return f"{self.kg} kg"


class Resus(models.Model):
    resus = models.CharField(max_length=5)

    def __str__(self):
        return self.resus


class Couleur(models.Model):
    couleur = models.CharField(max_length=50)

    def __str__(self):
        return self.couleur


class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Importance(models.Model):
    importance = models.CharField(max_length=50)

    def __str__(self):
        return self.importance


class Acteur(models.Model):
    acteur = models.CharField(max_length=100)

    def __str__(self):
        return self.acteur


class Manga(models.Model):
    manga = models.CharField(max_length=100)

    def __str__(self):
        return self.manga


class PEGI(models.Model):
    pegi = models.CharField(max_length=10)

    def __str__(self):
        return self.pegi


class Musique(models.Model):
    titre = models.CharField(max_length=100)
    album = models.CharField(max_length=100, null=True, blank=True)
    annee = models.ForeignKey("Annee", on_delete=models.SET_NULL, null=True)
    fichier = models.FileField(upload_to='musique/', null=True, blank=True)

    def __str__(self):
        return self.titre


class Annee(models.Model):
    annee = models.IntegerField()

    def __str__(self):
        return str(self.annee)


class Mangaka(models.Model):
    mangaka = models.CharField(max_length=100)

    def __str__(self):
        return self.mangaka


class Editeur(models.Model):
    editeur = models.CharField(max_length=100)

    def __str__(self):
        return self.editeur


class Perso(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    surnom = models.CharField(max_length=50, null=True, blank=True)
    anniversaire = models.DateField(null=True, blank=True)
    taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True)
    poids = models.ForeignKey(Poids, on_delete=models.SET_NULL, null=True)
    resus = models.ForeignKey(Resus, on_delete=models.SET_NULL, null=True)
    couleur_cheveux = models.ForeignKey(Couleur, related_name='cheveux', on_delete=models.SET_NULL, null=True)
    couleur_yeux = models.ForeignKey(Couleur, related_name='yeux', on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    importance = models.ForeignKey(Importance, on_delete=models.SET_NULL, null=True)
    acteur = models.ForeignKey(Acteur, on_delete=models.SET_NULL, null=True)
    manga = models.ForeignKey(Manga, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class LiaisonPerso(models.Model):
    perso = models.ForeignKey(Perso, on_delete=models.CASCADE)
    taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True)
    poids = models.ForeignKey(Poids, on_delete=models.SET_NULL, null=True)
    resus = models.ForeignKey(Resus, on_delete=models.SET_NULL, null=True)
    cheveux = models.ForeignKey(Couleur, related_name='liaison_cheveux', on_delete=models.SET_NULL, null=True)
    yeux = models.ForeignKey(Couleur, related_name='liaison_yeux', on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    importance = models.ForeignKey(Importance, on_delete=models.SET_NULL, null=True)
    acteur = models.ForeignKey(Acteur, on_delete=models.SET_NULL, null=True)
    manga = models.ForeignKey(Manga, on_delete=models.SET_NULL, null=True)


class LiaisonManga(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    pegi = models.ForeignKey(PEGI, on_delete=models.SET_NULL, null=True)
    musique = models.ForeignKey(Musique, on_delete=models.SET_NULL, null=True)
    annee = models.ForeignKey(Annee, on_delete=models.SET_NULL, null=True)
    mangaka = models.ForeignKey(Mangaka, on_delete=models.SET_NULL, null=True)
    editeur = models.ForeignKey(Editeur, on_delete=models.SET_NULL, null=True)