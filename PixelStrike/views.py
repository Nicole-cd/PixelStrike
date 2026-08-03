from django.shortcuts import render

from .models import Genero, favoritos


def inicio(request):
    context = {
        'generos': Genero.objects.filter(activo=True),
        'misFavoritos': favoritos.objects.all().values(),
    }
    return render(request, 'index.html', context)


def enlaces(request):
    return render(request, 'enlaces.html')


def noticias(request):
    return render(request, 'noticias.html')


def resenas(request):
    return render(request, 'resenas.html')


def contactos(request):
    return render(request, 'contactos.html')
