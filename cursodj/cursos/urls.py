
from django.urls import path

from . import  views

urlpatterns = [
    path('lista-talleres/', views.lista_talleres, name='lista de talleres')
]