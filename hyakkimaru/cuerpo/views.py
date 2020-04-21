from django.shortcuts import render
from .models import parte
# Create your views here.
def lista_partes(request):
    partes = parte.objects.all()
    return render(request,'cuerpo/lista_partes.html',{'partes':partes})