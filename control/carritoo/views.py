from django.shortcuts import render,get_object_or_404
from .models import Producto
from .form import ProductForm
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.


def product_list(request):
    products = Producto.objects.all()
    return render(request, 'listar.html',{'producto':products})

def product_detalle(request, pk):
    product = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle.html', {'producto':product})


def product_nuevo(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000')
    else:
        form = ProductForm()
    return render(request, 'registrar.html',{'form': form},)

def product_editar(request, pk):
    products = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=products)
        if form.is_valid():
            products = form.save(commit=False)
            products.save()
            return HttpResponseRedirect('http://127.0.0.1:8000')
    else:
        form=ProductForm(instance=products)
        return render(request, 'actualizar.html',{'form':form})