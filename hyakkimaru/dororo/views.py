from django.shortcuts import render
from .models import objeto

# Create your views here.
def lista_objetos(request):
    objetos = objeto.objects.all()
    return render(request,'dororo/lista_objetos.html',{'objetos':objetos})