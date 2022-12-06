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
# Create your models here.