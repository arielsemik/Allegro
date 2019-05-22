from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, Category, ProductImages


def index(request):
    return HttpResponse('Strona z produktami')

def product_list(request, category = None, customer = None):
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category and customer:
        products = products.filter(category = category, customer= customer)
    elif customer:
        products = products.filter(customer= customer)
    elif category:
        products = products.filter(category = category)

    return render(request, 'products/productlist.html', {'cusatomer': customer, 'category': category, 'categories': categories, 'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available = True)
    product_image = get_object_or_404(ProductImages, product = id)
    seller = get_object_or_404(Product, id=id)
    return render(request, 'products/productdetails.html', {'product': product, 'image': product_image, 'seller': seller})

