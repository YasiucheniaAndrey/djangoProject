from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Product
from order.models import ProductInOrder, Order
from django.utils import timezone

class ProductListView(generic.ListView):
    template_name = 'product/products.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class ProductListViewByCategory(generic.ListView):
    template_name = 'product/products_by_category.html'
    model = Product


class ProdeuctDetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'

def add_to_cart(request, pk):

    if request.user.is_authenticated:

        if request.method == "POST":
            product = get_object_or_404(Product, pk=pk)
            order = Order.objects.filter(user=request.user, status=Order.NOT_PAID).last()

            if order is None:
                print(order)
                order = Order(user=request.user,
                              timestamp=timezone.now())
                order.save()
            product_in_order = ProductInOrder.objects.filter(order=order, product=product).last()
            print(product_in_order)

            if product_in_order is None:
                product_in_order = ProductInOrder(
                    product=product,
                    order=order,
                    quantity=1
                )
                product_in_order.save()
            else:
                product_in_order.quantity += 1
                product_in_order.save()
            return HttpResponseRedirect(reverse('product:detail', args=(product.pk,)))
    else:
        return HttpResponseRedirect(reverse('login'))
