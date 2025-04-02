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

![libreria](https://github.com/user-attachments/assets/0b234e97-762e-4ea4-af09-b13a4ea35c22)

![usuarios](https://github.com/user-attachments/assets/644d116b-2e49-4044-8a85-9a2834d95101)

![prestamos](https://github.com/user-attachments/assets/053bb1b3-9fef-49aa-b6e3-df2fde4e0338)


AHORA VAMOS A DAR UNA BREVE EXPLICACION DE LO QUE SERIA EL PROYECTO EN LA RAMA CREADA QUE SE LLAMA "SQL".

Rama SQL (Base de Datos Relacional)
Esta rama adapta el mismo sistema de gestión de biblioteca para usar una base de datos SQL en lugar de MongoDB. Las funcionalidades del CRUD son idénticas, pero la estructura de datos y las consultas siguen el modelo relacional.

🗂️ Estructura de Tablas (SQL)
Se crearon tres tablas:

1. Tabla libros

titulo (VARCHAR).

autor (VARCHAR).

cantidad_ejemplares (INT).

2. Tabla usuarios

nombre (VARCHAR).

correo (VARCHAR, UNIQUE).

celular (VARCHAR).

3. Tabla prestamos

dia (DATE o VARCHAR).

hora (TIME o VARCHAR).

libro (VARCHAR).

![sql libros](https://github.com/user-attachments/assets/61ca6bfe-f58f-4953-84fe-02c02cfcba40)

![sql usuarios](https://github.com/user-attachments/assets/aedac121-c9de-42c4-b231-a78827a2a9e0)

![sql prestamos](https://github.com/user-attachments/assets/9659f0c9-ab3c-4f4d-b0ae-b30d51ced583)

![heidi](https://github.com/user-attachments/assets/02bfdc3b-ee67-416b-97cb-320b7c70e837)


![gracias](https://github.com/user-attachments/assets/71035866-1aff-475d-b696-b4684262f1da)

