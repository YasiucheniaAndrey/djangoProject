from django.db import models
from django.conf import settings


class Product(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE
    )
    is_pesent = models.BooleanField(default=True)


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=50)


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    rating = models.SmallIntegerField()
    timestamp = models.DateTimeField()
    text = models.TextField()


class Order(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    PAID = 'order is paid'
    NOT_PAID = 'order is not paid'
    STATUS = [
        (PAID, 'order is not paid yet '),
        (NOT_PAID, 'order is paid')
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default = NOT_PAID
    )
    timestamp = models.DateTimeField()
