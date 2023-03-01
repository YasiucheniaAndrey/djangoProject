from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
#    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.ProdeuctDetailView.as_view(), name='detail'),
    path('', views.ProductListView.as_view()),
]
