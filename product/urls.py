from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('<int:pk>/', views.ProdeuctDetailView.as_view(), name='detail'),
    path('<int:pk>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('', views.ProductListView.as_view()),
]
