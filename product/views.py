from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Product

class IndexView(generic.ListView):
    template_name = 'product/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class ProdeuctDetailView(generic.DetailView):
    model = Product
#    queryset = Product.objects.all()
    template_name = 'product/detail.html'
#    context_object_name = 'product'
#    def get_context_data(self, 'pk'):
#        context = super().get_context_data('pk')



# def detail(request, pk):
#     product = get_object_or_404(Product,pk=pk)
#     context = {'product_description': product.description,
#                'product_short_description': product.short_description,
#                'product_price': product.price}
#     return render (request, 'product/detail.html', context)
