from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=50 , null=True)
    telephone = models.CharField(max_length=50 , null=True)
    date_creation = models.DateTimeField(auto_now=True , null=True)

    def __str__(self):
        return self.nom