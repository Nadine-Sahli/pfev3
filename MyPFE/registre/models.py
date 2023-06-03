from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.gis.admin import OSMGeoAdmin
from django.conf import settings
import datetime

from django.db import models
from django.utils import timezone

class Projet(models.Model):
    id = models.AutoField(primary_key=True)
    Nom_projet = models.CharField(max_length=100)
    Nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    NB_GSM = models.IntegerField(default=000)
    pseudo = models.CharField(max_length=100)
    e_mail = models.EmailField(max_length=100)
    reference = models.CharField(max_length=100)
    password = models.CharField(max_length=200, default='default-password')
    composteur = models.ForeignKey('composteur', on_delete=models.CASCADE, null=True)

    # start_date = models.DateField(default=datetime.date(2023, 1, 1))
    # end_date = models.DateField(default=datetime.date(2023, 12, 31))

    def __str__(self):
        return self.Nom_projet   
    def delete_projet(self):
        # Ajoutez ici la logique de suppression du projet
        self.delete()
    def update_projet(self, **kwargs):
        # Ajoutez ici la logique de mise à jour du projet
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()    
class composteur(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    NB_GSM = models.CharField(max_length=100, null=True)
    pseudo = models.CharField(max_length=100, null=True)
    e_mail = models.EmailField(max_length=100, null=True)
    

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    
      
# class Projet(models.Model):
#     Nom_projet = models.CharField(max_length=100)
#     Nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     GSM = models.IntegerField(default=0)
#     pseudo = models.CharField(max_length=100)
#     e_mail = models.EmailField(max_length=100)
#     reference = models.CharField(max_length=100)
#     password = models.CharField(max_length=200, default='default-password')
#     start_date = models.DateField(default=timezone.now)
#     end_date = models.DateField(default=timezone.now)
#     comp = models.ForeignKey(composteur, on_delete=models.CASCADE, related_name='projets', default=1) # replace 1 with the default composteur object id

#     def __str__(self):
#         return self.nom_projet









# class composteur(models.Model):
   
#     nom = models.CharField(max_length=100, null=True)
#     prenom = models.CharField(max_length=100, null=True)
#     NB_GSM = models.CharField(max_length=100, null=True)
#     pseudo = models.CharField(max_length=100, null=True)
#     e_mail = models.EmailField(max_length=100, null=True)
#     composteur_id = models.CharField(max_length=100, null=True, unique=True)

#     def __str__(self):
#         return f"{self.prenom} {self.nom}"


class client(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    NB_GSM = models.CharField(max_length=100, null=True)
    pseudo = models.CharField(max_length=100, null=True)
    e_mail = models.EmailField(max_length=100, null=True)
    client_id = models.CharField(max_length=100, null=True, unique=True)
 

    def __str__(self):
        return f"{self.prenom} {self.nom}"

# class Projet(models.Model):
#     id = models.AutoField(primary_key=True)
#     Nom_projet = models.CharField(max_length=100)
#     Nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     NB_GSM = models.IntegerField()
#     pseudo = models.CharField(max_length=100)
#     e_mail = models.EmailField(max_length=100)
#     reference = models.CharField(max_length=100)
#     password = models.CharField(max_length=200, default='default-password')
#     start_date = models.DateField(default=datetime.date(2023, 1, 1))
#     end_date = models.DateField(default=datetime.date(2023, 12, 31))
#     comp = models.ForeignKey(composteur, on_delete=models.CASCADE, null=True, blank=True,related_name='%(class)s_related')

#     def __str__(self):
#         return self.Nom_projet





