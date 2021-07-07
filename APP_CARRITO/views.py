from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .carrito import Carrito
from APP_PRODUCTOS.models import Producto 

# Create your views here.

@login_required
def carrito(request):
    return render(request, 'carrito.html')

@login_required
def pronto(request):
    return render(request, 'pronto.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect("carrito")

def vaciar_carrito(request):
    carrito = Carrito(request)
    carrito.vaciar_carrito()
    return redirect("carrito")

