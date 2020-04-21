from django.db import models

# Create your models here.
class objeto(models.Model):
    nombre = models.CharField(max_length= 100, blank= False, null= False)
    procedencia = models.CharField(max_length= 100, blank= False, null= False)

def __srt__(self):
    return self.nombre