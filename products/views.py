from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from products.models import Product, Specification, Image, Category


def index(request):
    top_products = Product.objects.all()[:10]
    template = loader.get_template('index.html')
    context = {
        'products': top_products,
    }
    return HttpResponse(template.render(context, request))


def product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    specs = Specification.objects.get_specs_key_value(product_id)
    return render(request, 'product.html', {'product': product, 'specifications': specs})


def store(request):
    return render(request, 'store.html')
