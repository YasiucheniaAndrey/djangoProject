from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Product


def index(request):
    product_list = Product.objects.order_by('-id')
    context = {
        'product_list':product_list,
    }
    return render(request, 'product/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    context = {'pd': product.description,
               'psd': product.short_description,
               'pp': product.price}
    return render (request, 'product/detail.html', context)



