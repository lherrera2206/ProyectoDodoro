from django.urls import include, path
from .views import lista_demonios, demonio_print
urlpatterns = [
    path('lista_demonios/',lista_demonios, name= 'lista_demonios'),
    path('demonio_print/',demonio_print, name= 'Printear_demons'),
]
