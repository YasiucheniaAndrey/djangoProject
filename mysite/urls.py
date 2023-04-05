from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    path("categories/", views.CategoryView.as_view(), name='index'),
    path("brands_with_description/", views.BrandView.as_view(), name="brands_with_description"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls"))
]