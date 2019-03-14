from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import redirect

# Create your views here.

def store_home(request):
    productos = Producto.objects.all()
    return render(request, 'store/store_productos.html',{'productos':productos})

def producto_detalle(request, pk):
    # if request.method == 'POST':

    # else:
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'store/producto_detalle.html',{'producto':producto})