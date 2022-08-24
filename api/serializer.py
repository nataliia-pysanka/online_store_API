from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['title']
        model = Product
        fields = ('id', 'title', 'price')


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['date']
        model = Order
        fields = ('id', 'date', 'products')
