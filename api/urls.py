from api.views import OrderViewSet, ProductViewSet, StatsViewSet, \
    OrderDateViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'api/products', ProductViewSet, basename='product')
router.register(r'api/orders', OrderViewSet, basename='order')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/stats/', StatsViewSet.as_view()),

]
