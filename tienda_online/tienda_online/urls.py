"""tienda_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import inicio, clientes, pedidos, productos, contacto, anadir_producto, gracias_anadir, buscar_producto, registrar_cliente, registrar_pedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('clientes/', clientes, name='clientes'),
    path('pedidos/', pedidos, name='pedidos'),
    path('productos/', productos, name='productos'),
    path('productos/anadir_producto/', anadir_producto, name='anadir_producto'),
    path('productos/anadir_producto/gracias_anadir/', gracias_anadir, name='gracias_anadir'),
    path('productos/buscar_producto/', buscar_producto, name='buscar_producto'),
    path('contacto/', contacto, name='contacto'),
    path('clientes/registrar_cliente/', registrar_cliente, name='registrar_cliente'),
    path('pedidos/registrar_pedido/', registrar_pedido, name='registrar_pedido'),
]
