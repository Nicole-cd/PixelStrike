from django.db import models


class favoritos(models.Model):
    nombreFavorito = models.CharField(max_length=100)
    descripcionFavorito = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreFavorito

    class Meta:
        verbose_name = 'favorito'
        verbose_name_plural = 'favoritos'


class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['orden', 'nombre']


class Juego(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='juegos/', blank=True)
    categoria = models.CharField(max_length=50)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-destacado', 'titulo']


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_publicacion']
