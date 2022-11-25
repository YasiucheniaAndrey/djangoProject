from django.db import models


class Product(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.IntegerField()
    brand = models.IntegerField()


class Brand(models.Model):
    name = models.CharField()
    description = models.TextField()


class Category(models.Model):
    category = models.CharField()


class Review(models.Model):
    product_id = models.IntegerField()
    revie_text = models.TextField()


class User(models.Model):
    login_name = models.CharField()
    id_review = models.IntegerField()
    id_product_purcaised = models.IntegerField()
    id_product_added_to_cart = models.IntegerField()
