from django.db import models
from comptes.models import Entreprise
from commandes.models import Commande_

# Create your models here.
# Categorie, Article, Stock, Fournisseur
# importer : Commande_, Stock, Fournisseur, Category


class Fournisseur(Entreprise):
    actif = models.BooleanField(default=True)
    


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class Stock(models.Model):
    dateEntree = models.DateField()
    qteInitiale = models.FloatField(20, 2)
    qteActuelle = models.FloatField(20, 2)
    dateExpiration = models.DateField()


class Article(models.Model):
    articleName = models.CharField(max_length=100)
    commande_ = models.ForeignKey(Commande_, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.PROTECT)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
   






