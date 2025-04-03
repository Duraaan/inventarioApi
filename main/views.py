from rest_framework import viewsets
from main.models import Producto
from main.serializer import ProductoSerializer       
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer