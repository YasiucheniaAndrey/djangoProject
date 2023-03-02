from django.views import generic
from django.contrib.auth import login
from django.urls import reverse
from .models import Category
from django.shortcuts import render, redirect
from customauth.admin import UserCreationForm




def dashboard(request):
    return render(request, "mysite/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(request,
                      "mysite/register.html",
                      {"form": UserCreationForm}
                    )
    elif request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

class CategoryView(generic.ListView):
    template_name = 'mysite/categories.html'
    context_object_name = 'categories_list'

    def get_queryset(self):
        return Category.objects.all()

