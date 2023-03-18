from django.shortcuts import render
from django.http import HttpResponse
from core.models import Articulo, Cliente, Pedido
from core.forms import SearchProduct, RegisterClient, RegisterOrder, ContactForm


def inicio(request):
    return render(request, 'core/inicio.html')


def clientes(request):
    return render(request, 'core/clientes.html')


def pedidos(request):
    return render(request, 'core/pedidos.html')


def productos(request):
    return render(request, 'core/productos.html')


def anadir_producto(request):
    return render(request, 'core/anadir_producto.html')


def gracias_anadir(request):
    if request.POST:
        if request.POST['product'] and len(request.POST['product']) <= 30 and not request.POST['product'].isdigit():
            if request.POST['section'] and len(request.POST['section']) <= 20 and not request.POST['section'].isdigit():
                if request.POST['price'].isdigit() and request.POST['price'].isdigit():
                    producto = Articulo(nombre=request.POST['product'], seccion=request.POST['section'], precio=request.POST['price'])
                    producto.save()
                    return render(request, 'core/gracias_anadir.html')
                else:
                    return HttpResponse("Alguno de los datos esta mal")
            else:
                return HttpResponse("Alguno de los datos esta mal")
        else:
            return HttpResponse("Alguno de los datos esta mal")
    else:
        return HttpResponse("Alguno de los datos esta mal")
    

def buscar_producto(request):
    if request.method == "POST":
        articulo = request.POST
        formulario = SearchProduct(articulo)
        
        if formulario.is_valid():
            articulos = Articulo.objects.filter(nombre__icontains=articulo['nombre'])
            return render(request, 'core/producto_encontrado.html', {"query":articulo['nombre'], 'articulos':articulos})
        
        else:
            return HttpResponse("los datos que ingresaste no son validos")
        
    else:
        formulario = SearchProduct()
    
    return render(request, 'core/buscar_producto.html', {"form":formulario})
    
    


def contacto(request):
    if request.method == "POST":
        data = request.POST
        formulario = ContactForm(data)
        
        if formulario.is_valid():
            cliente = formulario.cleaned_data['nombre']
            return render(request, 'core/mensaje_enviado.html', {"cliente":cliente})
        
    else:
        formulario = ContactForm()
    return render(request, 'core/contacto.html', {"form":formulario})


def registrar_cliente(request):
    if request.method == "POST":
        cliente = request.POST
        formulario = RegisterClient(cliente)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            customer = Cliente(nombre=informacion['nombre'], direccion=informacion['direccion'], email=informacion['email'], telefono=informacion['telefono'])
            customer.save()
            return render(request, 'core/cliente_registrado.html')
        
    else:
        formulario = RegisterClient()

    return render(request, 'core/registrar_cliente.html', {"form":formulario})


def registrar_pedido(request):
    if request.method == "POST":
        pedido = request.POST
        formulario = RegisterOrder(pedido)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            order = Pedido(numero=informacion['numero'], fecha=informacion['fecha'], entregado=informacion['entregado'])
            order.save()
            return render(request, 'core/pedido_registrado.html')
        
    else:
        formulario = RegisterOrder()

    return render(request, 'core/registrar_pedido.html', {"form":formulario})