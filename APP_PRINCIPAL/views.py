from django.shortcuts import render
from APP_PRODUCTOS.models import Producto
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def principal(request):
    tres_productos = Producto.objects.all().order_by("-id")[0:3]
    resto_productos = Producto.objects.all().order_by("-id")[3:]

    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(resto_productos, 7)
        resto_productos = paginator.page(page)

    except:
        raise Http404

    data = {
            'tres_productos': tres_productos,
            'entity': resto_productos,
            'paginator': paginator,
            'page': request.GET.get('page', 1),
            }

    return render(request, './principal.html', data)

def acerca_de(request):
    return render(request, './acerca_de.html')

