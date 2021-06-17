from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse

from commande.forms import CommandForm
from .models import Commande


def list_commandes(request):
    return render(request,'commande/list_commande.html')


def ajouter_commande(request):
    form = CommandForm()
    if request.method=='POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html' , context)

def modifier_commande(request ,  pk):
    commande= Commande.objects.get(pk)
    
    form = CommandForm()
    if request.method=='POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html' , context)
