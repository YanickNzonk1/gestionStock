from django.db import models
from comptes.models import Entreprise
from commandes.models import Commande

# Create your models here.
# Categorie, Article, Stock, Fournisseur
# importer : Commande_, Stock, Fournisseur, Category





class Fournisseur(Entreprise):
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = "fournisseur"

    def __str__(self):
        return self.nomEntreprise
    


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName


class Stock(models.Model):
    dateEntree = models.DateField()
    qteInitiale = models.FloatField()
    qteActuelle = models.FloatField()
    dateExpiration = models.DateField()

    class Meta:
        db_table = "stock"

    def __str__(self):
        return "stock numero" + str(self.pk)


class Article(models.Model):
    articleName = models.CharField(max_length=100)
    commande = models.ForeignKey(Commande, on_delete=models.PROTECT, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.PROTECT)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.articleName










# =====================================================================================
# ====================    PARTIR D'ICI       ==========================================
# =====================================================================================




# class Fournisseur(Entreprise):
#     actif = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nomEntreprise
    


# class Category(models.Model):
#     categoryName = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.categoryName


# class Stock(models.Model):
#     dateEntree = models.DateField()
#     qteInitiale = models.FloatField(20, 2)
#     qteActuelle = models.FloatField(20, 2)
#     dateExpiration = models.DateField()

#     def __str__(self):
#         return "stock numero" + self.pk


# class Article(models.Model):
#     articleName = models.CharField(max_length=100)
#     commande_ = models.ForeignKey(Commande_, on_delete=models.PROTECT)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     fournisseur = models.ForeignKey(Fournisseur, on_delete=models.PROTECT)
#     stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
   
#     def __str__(self):
#         return self.articleName
