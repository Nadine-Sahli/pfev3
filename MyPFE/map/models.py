from django.db import models
from django.contrib.gis.db import models 
from django.contrib.gis.admin import OSMGeoAdmin
from registre.models import composteur
from registre.models import client
from registre.models import Projet

class nodes(models.Model):
    # Client = models.ForeignKey(client, on_delete=models.CASCADE, default=1)
    # Composteur = models.ForeignKey(composteur, on_delete=models.CASCADE, null=True, default=None)
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
    Position = models.PointField(null=True)
    Latitude = models.CharField(max_length=50, null=True, blank=True)
    Longitude = models.CharField(max_length=50, null=True, blank=True)
    proj = models.ForeignKey(Projet, on_delete=models.CASCADE, null=True, blank=True,related_name='%(class)s_related')
    
    def __str__(self):
        return "Node " + str(self.Name)

    class Meta:
        verbose_name_plural = "Nodes"
        verbose_name = "Node"













    






   
    

   




   

