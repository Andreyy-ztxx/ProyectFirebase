📚 Explicación sencilla del proyecto

Este proyecto es una aplicación de consola hecha en Python, que permite registrar y listar libros y estudiantes.

Toda la información se guarda en Firebase Realtime Database, una base de datos en la nube.

⚙️ ¿Cómo funciona el programa?

1️⃣ El usuario usa un menú en la consola para:

Registrar libros con una categoría (Ciencia, Literatura o Historia).

Registrar estudiantes.

Ver la lista de libros o estudiantes registrados.


2️⃣ Cuando se registra algo, el programa envía los datos a Firebase y los guarda en la nube.

Así, aunque cierres el programa, la información no se pierde.


3️⃣ La estructura del código está dividida en partes (modelo MVVM) para mantenerlo ordenado:


Domain/ → contiene las clases Libro y Estudiante.

Representan los datos básicos que se guardan.


Data/ → maneja la conexión con Firebase y las funciones para guardar o leer información.


firebase_config.py conecta con Firebase usando los datos del archivo .env.


repository.py contiene las funciones para agregar y listar libros o estudiantes.


Presentacion/ → tiene la lógica del programa (viewmodel.py).

Se encarga de validar los datos antes de enviarlos al repositorio.


UI/ → contiene la interfaz del usuario (console_view.py).

Muestra el menú, recibe entradas y llama a las funciones necesarias.


App/ → contiene el archivo principal (main.py) que ejecuta todo.


4️⃣ El archivo .env guarda la información de conexión con Firebase (URL y clave del servicio).

Esto mantiene las credenciales seguras y evita ponerlas directamente en el código.


5️⃣ El archivo serviceAccountKey.json es la clave que permite al programa conectarse a Firebase.

Se descarga desde la consola de Firebase y se guarda en la raíz del proyecto (nunca se sube a GitHub).


🧠 En resumen


main.py → ejecuta todo.


console_view.py → muestra el menú y pide los datos.


viewmodel.py → valida lo que el usuario escribe.


repository.py → guarda y lee los datos desde Firebase.

firebase_config.py → configura la conexión a Firebase.

models.py → define qué es un libro y qué es un estudiante.
