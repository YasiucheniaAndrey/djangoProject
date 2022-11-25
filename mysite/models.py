from django.db import models


class Product(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.IntegerField()
    brand = models.IntegerField()


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Category(models.Model):
    category = models.CharField(max_length=50)


class Review(models.Model):
    product_id = models.IntegerField()
    revie_text = models.TextField()


class User(models.Model):
    login_name = models.CharField(max_length=50)
    id_review = models.IntegerField()
    id_product_in_order = models.IntegerField()


class Order(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    is_paid = models.BooleanField()
    order_date = models.DateTimeField()
