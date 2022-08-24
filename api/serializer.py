from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['title']
        model = Product
        fields = ('id', 'title', 'price')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Product` instance, given the validated data.
    #     """
    #     instance = Product.objects.create(**validated_data)
    #     instance.save()
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Product` instance,
    #     given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.price = validated_data.get('price', instance.code)
    #     instance.save()
    #     return instance


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['date']
        model = Order
        fields = ('id', 'date', 'products')
