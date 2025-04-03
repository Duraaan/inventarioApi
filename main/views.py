from rest_framework import viewsets
from main.models import producto
from main.serializer import ProductoSerializer        

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer