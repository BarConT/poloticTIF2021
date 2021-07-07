from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import ProductoForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q

# Create your views here.

def visualizar(request, id):
    producto = Producto.objects.all().filter(id=id)

    data = {
            'producto': producto 
            }

    return render(request, 'visualizar.html', data)

@permission_required('APP_PRODUCTOS.add_producto')
def agregar(request):
    data = {
            'form': ProductoForm()
            }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado") 
            return redirect(to='principal')
        else:
            data["form"] = formulario
    return render(request, 'agregar.html', data)

@permission_required('APP_PRODUCTOS.change_producto')
def editar(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
            'form': ProductoForm(instance=producto)
            }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="principal")
        data["form"] = formulario

    return render(request, 'editar.html', data)

@permission_required('APP_PRODUCTOS.delete_producto')
def borrar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="principal")

def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)

    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 6)
        productos = paginator.page(page)

    except:
        raise Http404

    data = {
            'categoria': categoria,
            'entity': productos,
            'paginator': paginator,
            'page': request.GET.get('page', 1),
            }
    return render(request, 'categoria.html', data)

def buscar(request):

    queryset = request.GET.get("buscar")
    if queryset:
         productos = Producto.objects.filter(
           Q(titulo__icontains = queryset) |
           Q(descripcion__icontains = queryset)
                 ).distinct()

    data = {
            'productos': productos
            }

    return render(request, 'resultado.html', data)
