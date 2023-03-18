from django.contrib import admin
from core.models import Cliente, Articulo, Pedido

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Articulo)
admin.site.register(Pedido)