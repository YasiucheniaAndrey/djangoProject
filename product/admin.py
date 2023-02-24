from django.contrib import admin
from .models import Product, Review

#admin.site.register(Product)
admin.site.register(Review)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category", "brand", "short_description")
