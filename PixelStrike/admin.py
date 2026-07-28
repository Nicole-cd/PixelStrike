from django.contrib import admin
from .models import favoritos
# Register your models here.
class favoritosAdmin(admin.ModelAdmin):
    list_display = ('nombreFavorito', 'descripcionFavorito')

admin.site.register(favoritos, favoritosAdmin)