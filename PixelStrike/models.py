from django.db import models

# Create your models here.
class favoritos(models.Model):
    nombreFavorito = models.CharField(max_length=100)
    descripcionFavorito = models.CharField(max_length=255)