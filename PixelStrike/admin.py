from django.contrib import admin

from .models import Genero, Juego, Noticia, favoritos


class favoritosAdmin(admin.ModelAdmin):
    list_display = ('nombreFavorito', 'descripcionFavorito')
    search_fields = ('nombreFavorito', 'descripcionFavorito')


admin.site.register(favoritos, favoritosAdmin)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destacado')
    list_filter = ('categoria', 'destacado')
    search_fields = ('titulo', 'descripcion', 'categoria')


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
    readonly_fields = ('fecha_publicacion',)
