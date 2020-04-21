from django.db import models

# Create your models here.
class pelea(models.Model):
    ganador = models.CharField(max_length= 100, blank= False, null= False)
    lugar = models.CharField(max_length= 100, blank= False, null= False)
    demonio = models.CharField(max_length= 100, blank= False, null= False)