from django.shortcuts import render,redirect
from .models import Enseignant
from django.contrib.auth import login, authenticate

# Create your views here.

def listEnseignantWithCours(request):
    enseignant = Enseignant.objects.all()
    return render(request,"listEnseignant.html",{"enseignant":enseignant})


def signin(request):

    if(request.method == "POST"):
        username= request.POST['username']
        password= request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('list_cours')
        else:
            return redirect('login')


    return render(request, 'login.html',{})