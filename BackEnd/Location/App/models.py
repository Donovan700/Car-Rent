from django.db import models

# Create your models here.

class Location(models.Model):
    numloc = models.AutoField(primary_key=True)
    nom_loc = models.CharField(max_length=50)
    design_voiture = models.CharField(max_length=20)
    Nombre_Jours = models.IntegerField(max_length=15)
    Taux_Journalier = models.IntegerField(max_length=20)

    def __str__(self):
        return self.nom_loc