# Prueba técnica Softcode
Reto técnico para la empresa Softcode SL, el cual tiene como objetivo crear una pequeña aplicación con Django para listar y crear productos

# ¿En que consiste?

• La prueba consta de dos partes: preguntas teóricas y ejercicios prácticos.

• Se espera que el aspirante complete ambas partes de la prueba.

• Se recomienda utilizar el entorno de desarrollo Django para resolver los ejercicios
prácticos.

• Puede utilizar cualquier recurso en línea, como la documentación oficial de Django,
para ayudarle a completar la prueba.

• Una vez que haya completado la prueba, envíe el código fuente y las respuestas a
las preguntas teóricas en un enlace a un repositorio de Git.

# Respuesta a preguntas teóricas

- ¿Qué es Django y cuáles son sus principales características?
  
    Django es un framework de alto nivel con el lenguaje de programación Python, permite crear sitios webs seguros, mantenibles y escalables.

    Entre sus más principales características están:

    Completo: Django proporciona todo lo que los programadores necesitan y que pueden usar.

    Escalable: Funciona por componentes de manera que se puede dividir responsabilidades, eso quiere decir que cada componente funciona de manera independiente para ser modificados y escalados en el tiempo.

    Versátil: Con su gran documentación y comunidad a logrado implementarse a todo tipo de sistemas devolviendo cualquier tipo de dato necesario.

    Seguro: Ayuda a los desarrolladores a evitar varios errores comunes de seguridad al proveer un framework que ha sido diseñado para “hacer lo correcto” para proteger el sitio web automáticamente.

    Portátil: Permite funcionar con distintos motores de base de datos, plantillas y servidores.

    Mantenible: Siguiendo el principio "DRY", django permite modular la aplicación, por lo cual lo hace más facil su mantenibilidad en el tiempo.

- ¿Qué es un modelo en Django y cómo se define?

    Un modelo en Django es un tipo especial de objeto que se guarda en la base de datos y que representa una entidad o concepto del dominio de la aplicación.

    Para definir un modelo en Django, hay que seguir estos pasos:

    - Crear una aplicación dentro del proyecto Django con el comando python manage.py startapp nombre_app.

    - Editar el archivo models.py de la aplicación y escribir las clases que representan los modelos, siguiendo la sintaxis de Django.

    - Registrar la aplicación en el archivo settings.py del proyecto, añadiendo el nombre de la aplicación a la lista INSTALLED_APPS.

    - Ejecutar el comando python manage.py makemigrations nombre_app para generar los archivos de migración que contienen las instrucciones para crear las tablas de la base de datos a partir de los modelos.

    - Ejecutar el comando python manage.py migrate para aplicar las migraciones y crear las tablas en la base de datos automáticamente.

- Explica la diferencia entre una clave primaria (primary_key) y una clave foránea
(foreign_key) en Django.

    Una clave primaria (primary_key) es un campo o conjunto de campos que identifican de forma única a cada registro de una tabla en la base de datos, mientras que la clave foránea (foreign_key) es un campo o conjunto de campos que hacen referencia a la clave primaria de otra tabla, estableciendo así una relación entre ambas.

    En Django, se puede definir una clave primaria para un modelo usando el argumento primary_key=True en el campo correspondiente, mientras que la clave foránea se define la clase models.ForeignKey y se le pasa como primer argumento el modelo al que hace referencia, y como segundo argumento la acción que se debe tomar cuando se elimina el registro referenciado.

    Ejemplo:

``` from django.db import models

    class Libro(models.Model):
        isbn = models.CharField(max_length=13, primary_key=True) # Clave primaria
        titulo = models.CharField(max_length=200)
        autor = models.ForeignKey('Autor', on_delete=models.CASCADE) # Clave foránea

    class Autor(models.Model):
        nombre = models.CharField
```

- ¿Qué son las migraciones en Django y para qué se utilizan?

    Las migraciones en Django son archivos que contienen los cambios que se han hecho en los modelos y que se deben aplicar al esquema de la base de datos. Las migraciones sirven para mantener sincronizados los modelos y la base de datos, facilitando el desarrollo y el despliegue de las aplicaciones.

- ¿Qué es un middleware en Django y cómo se configura?

    Un middleware en Django es un componente que se engancha en el procesamiento de las peticiones y las respuestas, y que puede alterar la entrada o la salida de los endpoints. El middleware puede usarse para diversas funciones, como seguridad, sesión, protección CSRF y autenticación. Es un sistema de plugins ligero y de bajo nivel que se ejecuta en segundo plano.

    Para configurar el middleware en Django, hay que seguir estos pasos:

    - Escribir una clase o una función que cumpla con la API de middleware, aceptando un argumento get_response y devolviendo un invocable que tome una petición y devuelva una respuesta.

    - Añadir el nombre completo de la clase o la función al final de la lista MIDDLEWARE en el archivo settings.py del proyecto.

    - Ejecutar el comando python manage.py check para comprobar que no hay errores en la configuración del middleware.

    Ejemplo: 
    
  ```
  class SimpleMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response
            # Configuración e inicialización de una sola vez.

        def __call__(self, request):
            # Código a ejecutar para cada petición antes
            # de llamar a la vista (y al middleware posterior).
            print("Antes de la vista")

            response = self.get_response(request)

            # Código a ejecutar para cada petición/respuesta después
            # de llamar a la vista.
            print("Después de la vista")

            return response```

# Ejercicios prácticos

1. Crea un modelo llamado Producto que tenga los siguientes campos:
    • nombre (cadena de caracteres)
    • precio (número decimal)
    • descripcion (texto largo)
    • fecha_publicacion (fecha y hora)
    • activo (booleano)

2. Crea una vista basada en clase que liste todos los productos en una página web.
    La vista debe mostrar el nombre y el precio de cada producto.

3. Crea una URL que mapee a la vista anterior y verifica que la lista de productos se
    muestra correctamente en el navegador.

4. Agrega un formulario de creación de productos en la página de lista de productos.
    El formulario debe permitir al usuario ingresar el nombre, precio, descripción, fecha
    de publicación y estado del producto (activo/inactivo).
    
5. Crea una vista que muestre los detalles de un producto específico cuando se hace
    clic en su nombre en la lista de productos. La vista debe mostrar todos los campos
    del producto.
    
6. Agrega una URL que mapee a la vista de detalles del producto y verifica que los
    detalles se muestran correctamente en el navegador cuando se hace clic en un
    producto.

# Requisitos del entorno de proyecto

- Django
- django-bootstrap-v5
- django-browser-reload
- python-decouple

# Desarrollo

- Se usó la última versión de django actual (4.2.2) para el desarrollo del proyecto
- Para el frontend se usó Bootstrap con los íconos de fontawesome 5 importados al proyecto, para ser utilizados en el proyecto.
- Se decidió usar Docker para establecer la imagen en un contenedor y sea más fácil su uso en distintos sistemas.
- La base de datos usada es SQLite3.
- Se adaptaron 3 endpoints correspondientes a listar, detallar y crear productos.
- Cada vista es basada en clase.
- Se adaptaron tests unitarios para verificar el correcto funcionamiento del sistema.

# Instalación

- Por seguridad y para no mostrar datos sensibles a la hora de desplegar el código en GitHub, siguiendo parte de la metodología twelve-factor el archivo de configuración se establece con la variable de entorno de Django .env, el cuál está excluido del repositorio. Se debe crear el archivo .env en la raíz del proyecto y establecer tu SECRET_KEY para tu entorno, existe un archivo llamado .env.example de modo de ejemplo:

```SECRET_KEY = '....your secret key ....'```

- Para instalar el proyecto se usará Docker para hacer build de la imagen al contenedor.

- Una vez tengas instalado y encendido el entorno de docker, vete a la raíz del proyecto y ejecuta este comando para instalar la imagen de Python 3.11.3 y cada dependencia necesaria en el proyecto:

```docker compose build```

- Cuando finalice la instalación ejecuta el siguiente comando para correr el servidor:

```docker compose up```

- Ya corriendo el servidor dirígete a [http://localhost:8000/](url) y verás la aplicación corriendo

![image](https://github.com/kike1996luis/softcode/assets/44822982/5f29806b-def5-4984-9708-a09e1b5c2e4f)

# Tests unitarios

Este proyecto cuanto con un test unitario para verificar que el modelo de producto esté funcionando correctamente, para acceder a él solo ejecuta este comando:

```docker compose run web python manage.py test apps.products.tests.TestProductCase.products_ut```
