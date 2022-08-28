from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model data
    """
    id = serializers.IntegerField()
    title = serializers.StringRelatedField()
    price = serializers.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model data
    """
    id = serializers.IntegerField()
    date = serializers.DateTimeField(format="%Y-%m-%d")
    products = ProductSerializer(many=True)

    def get_or_create_products(self, products):
        """
        Creates new Product instances or gets already existed and
        returns list of them id's
        """
        products_ids = []
        for product in products:
            product_instance, created = Product.objects.get_or_create(
                pk=product.get('id'), defaults=product)
            products_ids.append(product_instance.pk)
        return products_ids

    def create_or_update_products(self, products):
        """
        Creates new Product instances or updates already existed and
        return list of them id's
        """
        products_ids = []
        for product in products:
            print('product ', product.values())
            product_instance, created = Product.objects.update_or_create(
                pk=product.get('id'), defaults=product)
            print(product_instance, created)
            products_ids.append(product_instance.pk)
        print('products_ids: ', products_ids)
        return products_ids

    def create(self, validated_data):
        """
        Creates and returns a new Order instance based on given validated data
        """
        products = validated_data.get('products', [])
        order = Order.objects.create(**validated_data)
        order.products.set(self.get_or_create_products(products))
        return order

    def update(self, instance, validated_data):
        """
        Updates and returns an existing Order instance based on given
        validated data
        """
        products = validated_data.get('products', [])
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
