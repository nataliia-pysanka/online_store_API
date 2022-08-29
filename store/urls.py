from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
]
