from django.shortcuts import render, redirect
from .forms import UtilisateurForm
from .models import Utilisateur
#from django.contrib.auth.forms import UserCreationForm 
#from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()

 
 



 

def connexion(request):
   pass
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('acceuil')
    #     else:
    #         messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    # return render(request, 'connexion.html')

#@login_required
def accueil(request):
    #pass
    return render(request, 'accueil.html')

def deconnexion(request):
    pass
    # logout(request)
    # return redirect('connexion')


def experts(request):
    return render(request, 'experts.html')