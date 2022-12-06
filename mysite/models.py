from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=50)




