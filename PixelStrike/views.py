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
    