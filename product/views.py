from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Product page")

def detail(request, product_id):
    return HttpResponse(product_id)
