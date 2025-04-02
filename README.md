02/04/25

Sistema de Gestión de Biblioteca (CRUD con MongoDB)

Este proyecto es un sistema de gestión de biblioteca que permite administrar libros, usuarios y préstamos mediante operaciones CRUD (Create, Read, Update, Delete).
Está desarrollado con una base de datos MongoDB y utiliza tres colecciones principales para organizar la información.

Finalidad del Proyecto
El sistema está diseñado para:

1.Gestionar el inventario de libros (títulos, autores y ejemplares disponibles).

2.Registrar y administrar usuarios de la biblioteca (datos personales y contacto).

3.Controlar préstamos de libros (fechas, horarios y dia del prestamo).

4.Ideal para bibliotecas pequeñas o medianas que necesitan una solución digital para organizar sus recursos.

Estructura de la Base de Datos

1. Colección gestion_de_libros
   
titulo (String): Título del libro.

autor (String): Autor del libro.

cantidad_de_ejemplares (Number): Número de copias disponibles.

2. Colección gestion_de_usuarios
   
nombre (String): Nombre completo del usuario.

correo (String): Correo electrónico.

celular (number): Número de teléfono.

3. Colección gestion_de_prestamos

dia (Date): Fecha del préstamo (ej. "YYYY-MM-DD").

hora (String): Hora del préstamo (ej. "HH:MM").

libro (String): Libro prestado.

Funcionalidades Principales (CRUD)

Libros:

Añadir nuevos libros al catálogo.

agregar/editar/eliminar libros existentes.

Actualizar la cantidad de ejemplares.

Usuarios:

Registrar nuevos usuarios.

Modificar o dar de baja usuarios.

Préstamos:

Registrar un préstamo (asociando libro y usuario).

Consultar préstamos activos.


Cómo Ejecutar el Proyecto

Clona el repositorio:

