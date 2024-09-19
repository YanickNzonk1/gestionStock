from django.db import models
#from comptes.models import Entreprise
#from produits.models import Article

# Create your models here.
#  Facture, Client, Commande, Detail




# class Client(Entreprise):
#     STATUT_CHOICES = (
#         ('Regulier', 'REG'),
#         ('Occasionnel', 'OCC'),
#     )
#     statut = models.CharField(max_length=3, choices=STATUT_CHOICES, default='F')
#     telephone = models.CharField(max_length=15)
#     actif = models.BooleanField(default=True)

#     class Meta:
#         db_table = "client"

#     def __str__(self):
#         return self.nomEntreprise
    

# class Commande(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.PROTECT)
#     dateCom = models.DateField(auto_now_add=True)
#     STATUT_CHOICES = (
#         ('Initiée', 'INI'),
#         ('En traitement', 'ENT'),
#         ('Traitée', 'TTE'),
#         ('Payée', 'PYE'),
#     )
#     statut = models.CharField(max_length=3, choices=STATUT_CHOICES, default='F')
#     # dateEcheance = models.DateField()    Champ calcule

#     class Meta:
#         db_table = "commande"

#     def __str__(self):
#         return "commande " + str(self.pk) + " " + self.client.nomEntreprise + " " + self.dateCom
    
    


#     # ====================================================================
#     # =============  FROM PRODUITS TO PREVENT CIRCULAR IMPORT ============
#     # ====================================================================

#     from comptes.models import Entreprise
# #from commandes.models import Commande, DetailCommande

# # Create your models here.
# # Categorie, Article, Stock, Fournisseur
# # importer : Commande_, Stock, Fournisseur, Category


 


# class Fournisseur(Entreprise):
#     actif = models.BooleanField(default=True)
#     isExternal = models.BooleanField(default=True)
#     class Meta:
#         db_table = "fournisseur"

#     def __str__(self):
#         return self.nomEntreprise
    


# class Category(models.Model):
#     categoryName = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)

#     class Meta:
#         db_table = "category"

#     def __str__(self):
#         return self.categoryName


# class Stock(models.Model):
#     dateEntree = models.DateField(auto_now_add=True)
#     qteInitiale = models.FloatField(default=100)
#     qteActuelle = models.FloatField(default=1)
#     dateExpiration = models.DateField(null=True, blank=True)

#     class Meta:
#         db_table = "stock"

#     def __str__(self):
#         return "stock numero" + str(self.pk)


# class Article(models.Model):
#     articleName = models.CharField(max_length=100)
#     prixUnitaire = models.FloatField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     fournisseur = models.ForeignKey(Fournisseur, on_delete=models.PROTECT, null=True, blank=True)
#     stock = models.ForeignKey(Stock, on_delete=models.PROTECT)

#     class Meta:
#         db_table = "article"

#     def __str__(self):
#         return self.articleName
    


    
# class DetailCommande(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.PROTECT) 
#     qte = models.FloatField(default=1)
#     commande = models.ForeignKey(Commande, models.PROTECT)

#     class Meta:
#         db_table = "detail"

#     def __str__(self):
#         return self.article.articleName + " " + str(self.qte)












#    =====================================================================================
#    ===========                   REPARTIR D'ICI                           ==============
#    =====================================================================================


# from django.db import models
# from comptes.models import Entreprise

# # Create your models here.
# #  Facture, Client, Commande_, Detail

# class Client(Entreprise):
#     statut = models.CharField(max_length=50)     # regulier/occasionnel
#     actif = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nomEntreprise

# class Commande_(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     dateCom = models.DateField()
#     statut = models.CharField(max_length=50)
#     dateEcheance = models.DateField()

#     def __str__(self):
#         return "commande numero" + self.pk

# class Facture(models.Model):
#     commande_ = models.ForeignKey(Commande_, on_delete=models.CASCADE) 
#     dateCreation = models.DateField()
#     dateEcheance = models.DateField()
#     isProformat = models.BooleanField(default=True)
#     statust = models.CharField(max_length=50)

#     def __str__(self):
#         return "Facture numero" + self.pk


# class Detail(models.Model):
#     Qte = models.FloatField(20, 2)
#     prixUnitaire = models.FloatField(20, 2)
#     facture = models.ForeignKey(Commande_, on_delete=models.CASCADE) 

#     def __str__(self):
#         return "Detail numero" + self.pk + "facture " + self.facture.pk






# class Facture(models.Model):
#     dateCreation = models.DateField(auto_now=True)
#     dateEcheance = models.DateField(null=True, blank=True)
#     isProformat = models.BooleanField(default=True)
#     statut = models.CharField(max_length=50)

#     class Meta:
#         db_table = "facture"

#     def __str__(self):
#         return "Facture numero" + str(self.pk)