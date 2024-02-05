
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Cliente, Factura, Producto, ProductoFactura
from .serializers import ClienteSerializer, FacturaSerializer, ProductoSerializer, ProductoFacturaSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import jwt
from django.views import View
from django.conf import settings
import csv
from django.http import HttpResponse
from io import StringIO
from datetime import timedelta, datetime 


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductoFacturaViewSet(viewsets.ModelViewSet):
    queryset = ProductoFactura.objects.all()
    serializer_class = ProductoFacturaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class RegistroUsuarioAPIView(APIView):
    def post(self, request, format=None):
        data = request.data

        if User.objects.filter(email=data.get('email')).exists():
            return Response({"error": "Ya existe un usuario con este correo electrónico"}, status=status.HTTP_400_BAD_REQUEST)

        nuevo_usuario = User.objects.create_user(username=data.get('email'), email=data.get('email'), password=data.get('password'))

        nuevo_usuario.save()

        return Response("Usuario registrado exitosamente", status=status.HTTP_201_CREATED)


class IniciarSesionAPIView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        usuario = authenticate(username=email, password=password)

        if usuario is not None:
            token = jwt.encode({'email': email}, settings.SECRET_KEY, expires_delta=timedelta(hours=1)) 
            
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


class CargarCSVClientes(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        csv_file = request.FILES.get('archivo_csv')  # Utiliza get para manejar el caso de que no haya archivo
        if not csv_file:
            return Response("No se proporcionó ningún archivo CSV", status=status.HTTP_400_BAD_REQUEST)

        csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
        errors = []

        for row in csv_data:
            if len(row) >= 4:
                documento, nombre, apellido, email = row
                Cliente.objects.create(documento=documento, nombre=nombre, apellido=apellido, email=email)
            else:
                errors.append("La fila del CSV no tiene suficientes datos")

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Archivo CSV cargado exitosamente")


class DescargarCSVClientes(View):
    def get(self, request):
        # genera los datos del archivo CSV
        clientes = Cliente.objects.all().values('documento', 'nombre', 'apellido', 'email')
        datos = list(clientes)

        # Verifica si hay datos para descargar
        if not datos:
            return HttpResponse("No hay clientes para descargar")

        # Construye el contenido del archivo CSV en una cadena
        csv_buffer = StringIO()
        fieldnames = ['documento', 'nombre', 'apellido', 'email']

        writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
        writer.writeheader()

        for dato in datos:
            writer.writerow(dato)

        csv_content = csv_buffer.getvalue()

        # Construye la respuesta HTTP con el contenido del archivo CSV
        response = HttpResponse(csv_content, content_type='text/csv')

        # Configura el encabezado Content-Disposition para indicar la descarga
        response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

        return response