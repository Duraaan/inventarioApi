from rest_framework import routers
from .views import ProductoViewSet

routers = routers.DefaultRouter()
routers.register('productos', ProductoViewSet, basename='productos')
urlpatterns = routers.urls