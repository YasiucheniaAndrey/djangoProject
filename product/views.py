from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Product
from order.models import ProductInOrder, Order
from django.utils import timezone
from .forms import CartForm

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
    def render_to_response(self, context, **response_kwargs):
        context["form"] = CartForm()
        return super(ProdeuctDetailView, self).render_to_response(context, **response_kwargs)

def add_to_cart(request, pk):

    if request.user.is_authenticated:

        if request.method == "POST":
            product = get_object_or_404(Product, pk=pk)
            form = CartForm(request.POST)
            if form.is_valid():
                order = Order.objects.filter(user=request.user, status=Order.NOT_PAID).last()

                if order is None:
                    print(order)
                    order = Order(user=request.user,
                                  timestamp=timezone.now())
                    order.save()
                product_in_order = ProductInOrder.objects.filter(order=order, product=product).last()

                if product_in_order is None:
                    product_in_order = ProductInOrder(
                        product=product,
                        order=order,
                        quantity=1
                    )
                    product_in_order.save()
                else:
                    product_in_order.quantity += form.cleaned_data['quantity']
                    product_in_order.save()
                return HttpResponseRedirect(reverse('product:detail', args=(product.pk,)))
            else:
#todo add error message if qantity <= 0 переделать форму и добавить ошибку
                context = {'form': form, 'product':product}
               # return HttpResponseRedirect(reverse('product:detail', args=(product.pk, )))
                return render(request, 'product/detail.html', context)
    else:
        return HttpResponseRedirect(reverse('login'))
