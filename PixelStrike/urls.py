from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('enlaces',views.enlaces, name="enlaces"), 
    path('noticias',views.noticias,name="noticias"),
    path('reseñas',views.reseñas,name="reseñas"),
    path('contactos',views.contactos,name="contactos"),
]