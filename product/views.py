from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Product

class ProductListView(generic.ListView):
    template_name = 'product/products.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class ProductListViewByCategory(generic.ListView):
    template_name = 'product/products_by_category.html'
    model = Product

    # def get_queryset(self, *args, **kwargs):
    #     qs = super(ProductListViewByCategory, self).get_queryset()
    #     qs = qs.order_by("-id")
    #     return qs



class ProdeuctDetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'

