from django.db import models
from client.models import Client
from produit.models import Produit

class Commande(models.Model):

    client = models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)
    produit=  models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL)
    date_creation = models.DateTimeField(auto_now_add=True)
