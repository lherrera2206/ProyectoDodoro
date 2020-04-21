from django.urls import include, path
from .views import lista_objetos
urlpatterns = [
    path('lista_objetos/',lista_objetos, name= 'lista_objetos')
]