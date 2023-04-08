from django.contrib import admin
from .models import Categoria, DetalleVenta, Juego, MetodoPago, Usuario, Venta

# Register your models here.
admin.site.register(Categoria)
admin.site.register(DetalleVenta)
admin.site.register(Juego)
admin.site.register(MetodoPago)
admin.site.register(Usuario)
admin.site.register(Venta)

