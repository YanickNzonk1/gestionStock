from django.contrib import admin
# from comptes.models import Utilisateur, Local, Entreprise, Representant, Vendeur, Contrat
# from commandes.models import Client, Commande, DetailCommande, Fournisseur, Category, Stock, Article

# # Register your models here.


# # Utilisateur
# class UtilisateurAdmin(admin.ModelAdmin):
#     list_display = ("userName", "passWord", "isAdmin", "createdBy", "inscriptionDate", "actif")

# admin.site.register(Utilisateur, UtilisateurAdmin)


# #Entreprise
# class EntrepriseAdmin(admin.ModelAdmin):
#     list_display = ("nomEntreprise", "adresse", "ville", "pays", "telephone")

# admin.site.register(Entreprise, EntrepriseAdmin)


# #Representant
# class RepresentantAdmin(admin.ModelAdmin):
#     list_display = ("entreprise", "nom", "prenom", "telephone")

# admin.site.register(Representant, RepresentantAdmin)


# #Vendeur
# class VendeurAdmin(admin.ModelAdmin):
#     list_display = ("nom", "prenom", "telephone")

# admin.site.register(Vendeur, VendeurAdmin)


# #Contrat
# class ContratAdmin(admin.ModelAdmin):
#     list_display = ("contenu", "vendeur", "representant", "dateSignature")

# admin.site.register(Contrat, ContratAdmin)


# #Local
# class LocalAdmin(admin.ModelAdmin):
#     list_display = ("description", "statut", "contrat", "actif")

# admin.site.register(Local, LocalAdmin)


# #Client
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ("nomEntreprise", "statut", "actif", "adresse", "ville", "pays", "telephone")

# admin.site.register(Client, ClientAdmin)



# #Commande
# class CommandeAdmin(admin.ModelAdmin):
#     list_display = ("client", "dateCom", "statut")

# admin.site.register(Commande, CommandeAdmin)


# #DetailCommande
# class DetailCommandeAdmin(admin.ModelAdmin):
#     list_display = ("article", "qte")

# admin.site.register(DetailCommande, DetailCommandeAdmin)


# #Fournisseur
# class FournisseurAdmin(admin.ModelAdmin):
#     list_display = ("nomEntreprise", "adresse", "ville", "pays", "telephone")

# admin.site.register(Fournisseur, FournisseurAdmin)


# #Category
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("categoryName", "description")

# admin.site.register(Category, CategoryAdmin)


# #Stock
# class StockAdmin(admin.ModelAdmin):
#     list_display = ("dateEntree", "qteInitiale", "qteActuelle", "dateExpiration")

# admin.site.register(Stock, StockAdmin)



# #article
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ("articleName", "category", "fournisseur")

# admin.site.register(Article, ArticleAdmin)

