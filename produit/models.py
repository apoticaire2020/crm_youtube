from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=50 , null=True)
    prix = models.FloatField(null=True)

    def __str__(self):
        return self.nom
