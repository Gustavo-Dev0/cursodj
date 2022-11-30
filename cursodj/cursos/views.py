from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cursos.models import Taller


def lista_talleres(request):
    talleres=Taller.objects.all()
    return HttpResponse(talleres)