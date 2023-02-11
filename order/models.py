from django.db import models
from product.models import Product
from django.conf import settings

class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    PAID = 'paid'
    NOT_PAID = 'not paid'
    STATUS = [
        (PAID, 'order is paid '),
        (NOT_PAID, 'order is not paid')
    ]
    status = models.CharField(
        max_length = 20,
        choices = STATUS,
        default = NOT_PAID
    )
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.product.short_description

