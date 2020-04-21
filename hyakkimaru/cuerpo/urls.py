from django.urls import include, path
from .views import lista_partes
urlpatterns = [
    path('lista_partes/',lista_partes, name= 'lista_partes')
]