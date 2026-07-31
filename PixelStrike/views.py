from django.shortcuts import render

from .models import Genero, Juego, Noticia, favoritos


def inicio(request):
    context = {
        'generos': Genero.objects.filter(activo=True),
        'misFavoritos': favoritos.objects.all()[:5],
        'juegosDestacados': Juego.objects.filter(destacado=True),
    }
    return render(request, 'index.html', context)


def enlaces(request):
    return render(request, 'enlaces.html')


def noticias(request):
    return render(request, 'noticias.html', {'noticias': Noticia.objects.all()})


def resenas(request):
    return render(request, 'resenas.html', {'juegos': Juego.objects.all()})


def contactos(request):
    return render(request, 'contactos.html')
