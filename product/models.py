from django.db import models
from django.conf import settings
from mysite.models import Category, Brand

class Product(models.Model):
    #past method with short name  str__
    # list display
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

    def __str__(self):
        return self.short_description


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

    def __str__(self):
        return self.product
