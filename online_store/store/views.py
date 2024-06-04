from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForms

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForms()
    return render(request, 'product_create.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForms(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForms(instance=product)
    return render(request, 'product_update.html', {'form': form})