from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from api.views import OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'api/products', ProductViewSet, basename='product')
router.register(r'api/orders', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-token-auth/', obtain_auth_token, name='api-token-auth')
]
