from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Order(models.Model):
    date = models.DateTimeField(default=timezone.now,
            blank=False, null=False)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.date)
