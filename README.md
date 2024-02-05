# quick
usuario admin
contraseña admin1

despliegue de la api:

1) ~/Ruta/del/archivo: source env/bin/activate
 activación del entorno virtual desde el directorio principal del proyecto
       
2) ~/Ruta/del/archivo/prueba$ python3 manage.py runserver	
 correr programa con pythone desde el directorio prueba
       
3) ingreso a la url http://127.0.0.1:8000/auth-token/
enviar petición POST en formato json con los datos de usuario y contraseña.
{
"username": "admin",
"password": "admin1"
}


4) se recibe respuesta con el Token de seguridad

5) ingresa a la url http://127.0.0.1:8000/clientes/ enviando una petición GET con la cabecera “Autorization” y el valor “Token + token recibido”, para acceder a la información de los clientes registrados en la BD.
Repetir esta cabecera para el resto de peticiones realizadas para cada url seleccionada.



links: 

clientes/: Esta URL corresponde a la vista ClienteViewSet. Cuando se hace una solicitud GET a esta URL, se devuelve una lista de todos los clientes. Cuando se hace una solicitud POST, se crea un nuevo cliente.

clientes/<int:pk>/: Esta URL también corresponde a la vista ClienteViewSet. Cuando se hace una solicitud GET a esta URL con un ID de cliente específico, se devuelve la información detallada de ese cliente. Cuando se hace una solicitud PUT, se actualiza la información del cliente con el ID especificado. Cuando se hace una solicitud DELETE, se elimina el cliente con el ID especificado.

facturas/: Esta URL corresponde a la vista FacturaViewSet. Funciona de manera similar a la URL de clientes, pero para las facturas.

facturas/<int:pk>/: Esta URL también corresponde a la vista FacturaViewSet, y también funciona de manera similar a la URL de clientes, pero para las facturas específicas.

productos/: Esta URL corresponde a la vista ProductoViewSet. Funciona de manera similar a la URL de clientes, pero para los productos.

productos/<int:pk>/: Esta URL también corresponde a la vista ProductoViewSet, y también funciona de manera similar a la URL de clientes, pero para los productos específicos.

productosFactura/: Esta URL corresponde a la vista ProductoFacturaViewSet. Funciona de manera similar a la URL de clientes, pero para los productos en las facturas.

productosFactura/<int:pk>/: Esta URL también corresponde a la vista ProductoFacturaViewSet, y también funciona de manera similar a la URL de clientes, pero para los productos en las facturas específicos.

cargar-csv-clientes/: Esta URL corresponde a la vista CargarCSVClientes. Se utiliza para cargar datos de clientes desde un archivo CSV.

descargar-csv/: Esta URL corresponde a la vista DescargarCSVClientes. Se utiliza para descargar los datos de clientes en formato CSV.

registro-usuario/: Esta URL corresponde a la vista RegistroUsuarioAPIView. Se utiliza para registrar un nuevo usuario en el sistema.

iniciar-sesion/: Esta URL corresponde a la vista IniciarSesionAPIView. Se utiliza para iniciar sesión en el sistema.

