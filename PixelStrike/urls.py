from django.contrib.auth import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('enlaces',views.enlaces, name="enlaces"), 
    path('noticias',views.noticias,name="noticias"),
    path('resenas', views.resenas, name="resenas"),
    path('contactos',views.contactos,name="contactos"),
]
