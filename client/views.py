from django.shortcuts import render
from django.http import HttpResponse
from .models import Client


def list_clients(request , pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    total_commande=commande.count()
    context={'client':client , 'commande':commande , 'total_commande':total_commande }
    return render(request,'client/liste_client.html' , context)
