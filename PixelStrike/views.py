from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import favoritos

# Create your views here.
def inicio(request):
    misFavoritos = favoritos.objects.all().values()
    template = loader.get_template('index.html')
    context = {'misFavoritos': misFavoritos}
    return HttpResponse(template.render(context,request))

def enlaces(request):
    template = loader.get_template('enlaces.html')
    return HttpResponse(template.render())

def noticias(request):
    template = loader.get_template('noticias.html')
    return HttpResponse(template.render())

def reseñas(request):
    template = loader.get_template('reseñas.html')
    return HttpResponse(template.render())

def contactos(request):
    template = loader.get_template('contactos.html')
    return HttpResponse(template.render())