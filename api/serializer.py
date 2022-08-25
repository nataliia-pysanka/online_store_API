from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class OrderSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")
    products = ProductSerializer(many=True)

    def get_or_create_products(self, products):
        products_ids = []
        for product in products:
            product_instance, created = Product.objects.get_or_create(
                pk=product.get('id'), defaults=product)
            products_ids.append(product_instance.pk)
        return products_ids

    def create_or_update_products(self, products):
        products_ids = []
        for product in products:
            product_instance, created = Product.objects.update_or_create(
                pk=product.get('id'), defaults=product)
            products_ids.append(product_instance.pk)
        return products_ids

    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        products = validated_data.get('products', [])
        order = Order.objects.create(**validated_data)
        order.products.set(self.get_or_create_products(products))
        return order

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance,
        given the validated data.
        """
        products = validated_data.get('products', [])
        print('products:', products)
        print('validated_data:', validated_data)
        instance.products.set(self.create_or_update_products(products))
        fields = ['date']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass
        instance.save()
        return instance

    class Meta:
        ordering = ['date']
        model = Order
        fields = ('id', 'date', 'products')

        extra_kwargs = {'products': {'required': False}}
