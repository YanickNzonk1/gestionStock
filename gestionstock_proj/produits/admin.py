from django.contrib import admin
from comptes.models import Utilisateur, Local, Entreprise, Representant, Vendeur, Contrat
from commandes.models import Client, Commande, Facture, Detail
from produits.models import Fournisseur, Category, Stock, Article
# Register your models here.


# Utilisateur
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ("userName", "passWord", "isAdmin", "createdBy", "inscriptionDate", "actif")

admin.site.register(Utilisateur, UtilisateurAdmin)


#Entreprise
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ("nomEntreprise", "adresse", "ville", "pays", "telephone")

admin.site.register(Entreprise, EntrepriseAdmin)


#Representant
class RepresentantAdmin(admin.ModelAdmin):
    list_display = ("entreprise", "nom", "prenom", "telephone")

admin.site.register(Representant, RepresentantAdmin)


#Vendeur
class VendeurAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "telephone")

admin.site.register(Vendeur, VendeurAdmin)


#Contrat
class ContratAdmin(admin.ModelAdmin):
    list_display = ("contenu", "vendeur", "representant", "dateSignature", "echeance")

admin.site.register(Contrat, ContratAdmin)


#Local
class LocalAdmin(admin.ModelAdmin):
    list_display = ("description", "statut", "contrat", "actif")

admin.site.register(Local, LocalAdmin)


#Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ("nomEntreprise", "statut", "actif", "adresse", "ville", "pays", "telephone")

admin.site.register(Client, ClientAdmin)



#Commande
class CommandeAdmin(admin.ModelAdmin):
    list_display = ("client", "dateCom", "statut", "dateEcheance")

admin.site.register(Commande, CommandeAdmin)


# Facture
class FactureAdmin(admin.ModelAdmin):
    list_display = ("commande", "dateCreation", "dateEcheance", "isProformat", "statut")

admin.site.register(Facture, FactureAdmin)



#Detail
class DetailAdmin(admin.ModelAdmin):
    list_display = ("article", "Qte", "prixUnitaire")

admin.site.register(Detail, DetailAdmin)


#Fournisseur
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ("nomEntreprise", "adresse", "ville", "pays", "telephone")

admin.site.register(Fournisseur, FournisseurAdmin)


#Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryName", "description")

admin.site.register(Category, CategoryAdmin)


#Stock
class StockAdmin(admin.ModelAdmin):
    list_display = ("dateEntree", "qteInitiale", "qteActuelle", "dateExpiration")

admin.site.register(Stock, StockAdmin)



#article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("articleName", "commande", "category", "fournisseur")

admin.site.register(Article, ArticleAdmin)

