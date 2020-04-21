from django.urls import include, path
from .views import lista_peleas
urlpatterns = [
    path('lista_peleas/',lista_peleas, name= 'lista_peleas')
]