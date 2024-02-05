from rest_framework import serializers
from .models import Cliente, Factura, Producto, ProductoFactura

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoFactura
        fields = '__all__'
