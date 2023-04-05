from django.contrib import admin
from django.urls import path
from .views import index, aventura, plataforma, guerra, terror, rpg, loggin, formulario

urlpatterns = [
    path('', index, name='index'),
    path('loggin/', loggin, name='loggin'),
    path('formulario/', formulario, name='formulario'),
    #catalogo de videojuegos
    path('catalogo/aventura/', aventura, name='aventura'),
    path('catalogo/plataforma/', plataforma, name='plataforma'),
    path('catalogo/guerra/', guerra, name='guerra'),
    path('catalogo/terror/', terror, name='terror'),
    path('catalogo/rpg/', rpg, name='rpg'),
]

