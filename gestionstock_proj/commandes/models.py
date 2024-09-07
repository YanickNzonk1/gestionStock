from django.db import models
from comptes.models import Entreprise

# Create your models here.
#  Facture, Client, Commande_, Detail



class Client(Entreprise):
    statut = models.CharField(max_length=50)     # regulier/occasionnel
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = "client"

    def __str__(self):
        return self.nomEntreprise

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateCom = models.DateField()
    statut = models.CharField(max_length=50)
    dateEcheance = models.DateField()

    class Meta:
        db_table = "commande"

    def __str__(self):
        return "commande numero" + str(self.pk)

class Facture(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE) 
    dateCreation = models.DateField()
    dateEcheance = models.DateField()
    isProformat = models.BooleanField(default=True)
    statut = models.CharField(max_length=50)

    class Meta:
        db_table = "facture"

    def __str__(self):
        return "Facture numero" + str(self.pk)


class Detail(models.Model):
    Qte = models.FloatField()
    prixUnitaire = models.FloatField()
    facture = models.ForeignKey(Commande, on_delete=models.CASCADE)
    article = models.CharField(max_length=50, default="Crayon a bille")

    class Meta:
        db_table = "detail"

    def __str__(self):
        return self.article










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

