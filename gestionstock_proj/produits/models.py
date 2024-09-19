from django.db import models










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
