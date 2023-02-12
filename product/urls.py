from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
#cant change adress to spefifics/product_id
#path specifics/<int:product_id>
#with change in index.html
# #<li><a href="{% url 'product:detail' product.id %}
]