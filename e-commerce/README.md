# Tienda Online (abstracta)

Plantilla de tienda online siguiendo una arquitectura limpia.

## Estructura básica de carpetas

```md
e-commerce/
|
|-- core/
|   |-- entities/          # Objetos de dominio puro (Producto, Usuario, Carrito, Orden, etc.)
|   |-- use_cases/         # Lógica de negocio principal (AgregarProducto, RealizarOrden, etc.)
|
|-- application/
|   |-- services/              # Servicios de aplicación que coordinan los casos de uso y las interfaces
|   |-- dtos/                  # Objetos de Transferencia de Datos para comunicación entre capas
|
|-- adapters/
|   |-- api/
|   |   |-- routers/           # Rutas FastAPI
|   |   |-- schemas/           # Modelos Pydantic para validación de API
|   |   |-- middlewares/       # Middlewares específicos de la API
|   |
|   |-- db/
|   |   |-- models/            # Modelos SQLAlchemy
|   |   |-- repositories/      # Implementaciones de repositorios que interactúan con la base de datos
|   |
|   |-- third_party/           # Código para interactuar con servicios externos (pasarelas de pago, envío, etc.)
|
|-- infrastructure/
|   |-- config/                # Configuraciones (base de datos, variables de entorno, etc.)
|   |-- main.py                # Punto de entrada principal (creación de la aplicación FastAPI)
|   |-- utils/                 # Utilidades generales (criptografía, manejo de fechas, etc.)
|   |-- views/                 # Vista de UI
|
|-- tests/
|   |-- unit/                  # Pruebas unitarias
|   |-- integration/           # Pruebas de integración
|
|-- docs/                      # Documentación
|-- .gitignore
|-- README.md
|-- pyproject.toml             # Dependencias (si estás usando Poetry)

```
## Entidades

User: Representa a un usuario del sistema.

Atributos: ID, username, email, password.
Métodos: verify_password.
Product: Representa un producto en venta.

Atributos: ID, name, description, price, stock_quantity.
Métodos: Ninguno, a menos que haya una lógica de negocio específica.
Cart: Representa el carrito de compras de un usuario.

Atributos: ID, user_id, list of Product IDs, total_price.
Métodos: add_product, remove_product.
Order: Representa una orden de compra realizada por un usuario.

Atributos: ID, user_id, list of Product IDs, total_price, status.
Métodos: place_order.
Category: Representa una categoría de productos.

Atributos: ID, name, list of Product IDs.
Métodos: Ninguno, a menos que haya una lógica de negocio específica.
Payment: Representa un pago realizado por un usuario.

Atributos: ID, user_id, order_id, amount.
Métodos: process_payment.


> Para más info leer la documentación en /documentation & test/docs/


## Contactame

[linkedIn](https://linkedin.com/in/perezcatriel)