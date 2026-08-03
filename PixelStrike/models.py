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



