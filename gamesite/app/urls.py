from django.contrib import admin
from django.urls import path, include
from .views import index, registro, categoria, perfil
from django.contrib.auth import views as auth_views
from .views import MyPasswordChangeView, CategoriaViewSet
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
router.register('categoria', CategoriaViewSet)

urlpatterns = [
    path('', index, name='index'),
    # catalogo de videojuegos
    path('catalogo/<str:nombre>/', categoria, name='categoria'),
    # registro
    path('registro/', registro, name='registro'),
    
    path('perfil/', perfil, name='perfil'),
    
    # cambiar contraseña
    path(
        'password_change/',
        MyPasswordChangeView.as_view(),
        name='password_change'),
    # rest_framework
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
