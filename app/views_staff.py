from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from . import db
from . models import Comic
from .forms import ComicForm


def home(request):
    return render(request, 'staff/staff_home.html')

def listProduct(request):
    keyword = request.GET.get('keyword', '')
    products = db.getProducts(keyword)
    return render(request, 'staff/product_list.html', {'products' : products, 'keyword' : keyword})

def addProduct(request):
    backURL = request.GET.get('back_url', reverse_lazy('listProduct'))
    form = ComicForm()
    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(backURL)

    return render(request, 'staff/product.html', {'form' : form, 'backURL': backURL})

def editProduct(request, id):
    backURL = request.GET.get('back_url', reverse_lazy('listProduct'))
    product = db.findProductById(id)
    form = ComicForm(instance=product)
    form.initial['id'] = id

    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(backURL)

    return render(request, 'staff/product.html', {'form' : form, 'backURL': backURL})

def deleteProduct(request, id):
    backURL = request.GET.get('back_url', reverse_lazy('listProduct'))
    product = get_object_or_404(Comic, pk=id)
    if product:
        product.delete()
    return redirect(backURL)