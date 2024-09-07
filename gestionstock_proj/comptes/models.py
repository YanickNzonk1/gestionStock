from django.db import models





# Create your models here.
#  utilisateur, vendeur, entreprise, contrat, local




class Utilisateur(models.Model):
    userName = models.CharField(max_length=100)
    passWord = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    createdBy = models.IntegerField(null=True, blank=True)
    inscriptionDate = models.DateField()
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = "utilisateur"

    def __str__(self):
        return self.userName



class Entreprise(models.Model):
    nomEntreprise = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    class Meta:
        db_table = "entreprise"

    def __str__(self):
        return self.nomEntreprise


class Representant(Utilisateur):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

    class Meta:
        db_table = "representant"

    def __str__(self):
        return self.prenom + " " + self.nom

class Vendeur(Utilisateur):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    class Meta:
        db_table = "vendeur"

    def __str__(self):
        return self.prenom + self.nom

class Contrat(models.Model):
    contenu =  models.CharField(max_length=2000)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.PROTECT)
    representant = models.ForeignKey(Representant, on_delete=models.PROTECT)
    dateSignature = models.DateField()
    echeance = models.DateField()

    class Meta:
        db_table = "contrat"

    def __str__(self):
        return 'Contrat numero' + str(self.pk)


class Local(models.Model):
    description =  models.CharField(max_length=500)
    statut = models.CharField(max_length=50)
    contrat = models.ForeignKey(Contrat, on_delete=models.PROTECT)
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = "local"

    def __str__(self):
        return "Local nuero" + self.pk














# ============================================================================================
# =======================     PARTIR D'ICI                        ============================
# ============================================================================================



# class Utilisateur(models.Model):
#     userName = models.CharField(max_length=100)
#     passWord = models.CharField(max_length=100)
#     isAdmin = models.BooleanField(default=False)
#     createBy = models.IntegerField(null=True)
#     inscriptionDate = models.DateField()
#     actif = models.BooleanField(default=True)

#     def __str__(self):
#         return self.userName



# class Entreprise(models.Model):
#     nomEntreprise = models.CharField(max_length=100)
#     adresse = models.CharField(max_length=200)
#     ville = models.CharField(max_length=100)
#     pays = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=20)

#     def __str__(self):
#         return self.nomEntreprise


# class Representant(Utilisateur):
#     entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=15)

#     def __str__(self):
#         return self.prenom + self.nom

# class Vendeur(Utilisateur):
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=20)

#     def __str__(self):
#         return self.prenom + self.nom

# class Contrat(models.Model):
#     contenu =  models.CharField(max_length=2000)
#     vendeur = models.ForeignKey(Vendeur, on_delete=models.PROTECT)
#     representant = models.ForeignKey(Representant, on_delete=models.PROTECT)
#     dateSignature = models.DateField()
#     echeance = models.DateField()
#     actif = models.BooleanField(default=True)

#     def __str__(self):
#         return 'Facture numero' + self.pk


# class Local(models.Model):
#     description =  models.CharField(max_length=500)
#     status = models.CharField(max_length=50)
#     contrat = models.ForeignKey(Contrat, on_delete=models.PROTECT)
#     actif = models.BooleanField(default=True)

#     def __str__(self):
#         return "Local nuero" + self.pk


