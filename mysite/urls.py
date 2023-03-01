from django.urls import path
from . import views
from django.conf.urls import include


#app_name = 'category'
urlpatterns = [
#    path('<int:pk>/', views.ProdeuctDetailView.as_view(), name='detail'),
    path("categories/", views.CategoryView.as_view(), name='index'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls"))
]