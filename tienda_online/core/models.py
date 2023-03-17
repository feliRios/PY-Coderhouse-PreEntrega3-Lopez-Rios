from django.db import models


class Cliente(models.Model):  # Tabla para los clientes
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)  # Campo opcional
    telefono = models.IntegerField()
    
    def __str__(self) -> str:
        return f"cliente {self.nombre} - id {self.id}"
    

class Articulo(models.Model):  # Tabla para los articulos de la tienda online
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f"article {self.nombre} - id {self.id}"
    
    
class Pedido(models.Model):  # Tabla para los pedidos
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self) -> str:
        return f"pedido {self.numero}"