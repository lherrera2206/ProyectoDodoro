from django.db import models

class demonio(models.Model):
    nombre = models.CharField(max_length= 100, blank= False, null= False)
    partecuerpo = models.CharField(max_length= 100, blank= False, null= False)
    ubicacion = models.CharField(max_length= 100, blank= False, null= False)

def __srt__(self):
    return self.nombre