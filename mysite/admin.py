from django.contrib import admin
from .models import Product, Review, Order, Category, Brand

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Brand)
# Register your models here.
