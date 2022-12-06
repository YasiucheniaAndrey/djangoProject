from django.db import models
from django.conf import settings
from mysite.models import Category, Brand

class Product(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )
    is_pesent = models.BooleanField(default=True)


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    rating = models.SmallIntegerField()
    timestamp = models.DateTimeField()
    text = models.TextField()
