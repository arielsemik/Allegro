from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, Category, ProductImages
from django.template import loader


def index(request):
    category_list = Category.objects.all()
    template = loader.get_template('products/index.html')
    context =  {'category_list': category_list}
    return HttpResponse(template.render(context, request))




def product_list(request, category_id = None):
    c = get_object_or_404(Category, pk=category_id)


    products = Product.objects.filter(available = True)
    template = loader.get_template('products/productlist.html')


    products = products.filter(product_category= category_id)
    context = {'products': products}
    return HttpResponse(template.render(context, request))

def product_detail(request, product_id):
    #product = get_object_or_404(Product, id=id, available = True)
    #product_image = get_object_or_404(ProductImages, product = id)
    #seller = get_object_or_404(Product, id=id)
    namep = get_object_or_404(Product, id = product_id)

    template = loader.get_template('products/productdetails.html')
    context = {'id': product_id, 'productname': namep.name}

    return HttpResponse(template.render(context, request))

