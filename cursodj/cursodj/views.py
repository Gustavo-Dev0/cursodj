from django.http import HttpResponse

def hello_django(request):
    return HttpResponse("Hola mundo Django 3.1.14")

def datos_personales(request):
    return HttpResponse("<h2>Dely Lazo Berreda - dlazoba@unsa.edu.pe</h2>")

def frase_dia(request):
    return HttpResponse("<p><strong>All que madruga Dios le ayuda</strong></p>")