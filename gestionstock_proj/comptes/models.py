from django.db import models


# Create your models here.
#  utilisateur, vendeur, entreprise, contrat, local

class Utilisateur(models.Model):
    userName = models.CharField(max_length=100)
    passWord = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    createBy = models.IntegerField(null=True)
    inscriptionDate = models.DateField()
    actif = models.BooleanField(default=True)



class Entreprise(models.Model):
    nomEntreprise = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)


class Representant(Utilisateur):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

class Vendeur(Utilisateur):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

class Contrat(models.Model):
    contenu =  models.CharField(max_length=2000)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.PROTECT)
    representant = models.ForeignKey(Representant, on_delete=models.PROTECT)
    dateSignature = models.DateField()
    echeance = models.DateField()
    actif = models.BooleanField(default=True)


class Local(models.Model):
    description =  models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    contrat = models.ForeignKey(Contrat, on_delete=models.PROTECT)
    actif = models.BooleanField(default=True)



    

