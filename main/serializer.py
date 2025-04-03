from rest_framework import serializers
from main.models import producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'