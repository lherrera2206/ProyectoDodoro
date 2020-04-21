from django.db import models

# Create your models here.
class parte(models.Model):
    nombre = models.CharField(max_length= 100, blank= False, null= False)
    estado = models.CharField(max_length= 100, blank= False, null= False)
    