from django.db import models
from comptes.models import Entreprise

# Create your models here.
#  Facture, Client, Commande_, Detail

class Client(Entreprise):
    statut = models.CharField(max_length=50)     # regulier/occasionnel
    actif = models.BooleanField(default=True)

class Commande_(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateCom = models.DateField()
    statut = models.CharField(max_length=50)
    dateEcheance = models.DateField()

class Facture(models.Model):
    commande_ = models.ForeignKey(Commande_, on_delete=models.CASCADE) 
    dateCreation = models.DateField()
    dateEcheance = models.DateField()
    isProformat = models.BooleanField(default=True)
    statust = models.CharField(max_length=50)


class Detail(models.Model):
    Qte = models.FloatField(20, 2)
    prixUnitaire = models.FloatField(20, 2)
    facture = models.ForeignKey(Commande_, on_delete=models.CASCADE) 
