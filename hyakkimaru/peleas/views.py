from django.shortcuts import render
from .models import pelea
# Create your views here.

def lista_peleas(request):
    peleas = pelea.objects.all()
    return render(request,'peleas/lista_peleas.html',{'peleas':peleas})