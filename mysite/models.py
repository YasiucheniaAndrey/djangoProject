from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




