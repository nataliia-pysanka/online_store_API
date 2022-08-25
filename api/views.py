from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import ProductSerializer, OrderSerializer
from .models import Product, Order
from rest_framework import filters
from rest_framework.views import APIView


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']


class StatsViewSet(viewsets.ModelViewSet):
    pass


# class ProductsListView(APIView):
#     """Displaying all products in the store on JSON"""
#     def get(self, request):
#         queryset = Product.objects.all()
#         if queryset:
#             serializer_for_queryset = ProductSerializer(
#                 instance=queryset,
#                 many=True
#             )
#             return Response(serializer_for_queryset.data,
#                             status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#
#