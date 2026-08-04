from django.contrib import admin

from .models import Genero, favoritos

class favoritosAdmin(admin.ModelAdmin):
    list_display = ('nombreFavorito', 'descripcionFavorito')
    search_fields = ('nombreFavorito', 'descripcionFavorito')

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)

admin.site.register(favoritos, favoritosAdmin)
admin.site.register(Genero, GeneroAdmin)
