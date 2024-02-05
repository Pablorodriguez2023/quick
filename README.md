# quick
usuario admin
contraseña admin1

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

