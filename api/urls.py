from api.views import OrderViewSet, ProductViewSet, StatsViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'api/products', ProductViewSet, basename='product')
router.register(r'api/orders', OrderViewSet, basename='order')
router.register(r'api/stats', StatsViewSet, basename='stats')

urlpatterns = [
    # path(r'api/stats/', StatsViewSet.as_view()),
    path(r'', include(router.urls)),

]
