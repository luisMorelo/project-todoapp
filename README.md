# project-todoapp
# project-todoapp
# project-todoapp


Para ejecutar un proyecto Django Todoapp:

1. Crear un entorno virtual: 
    Es recomendable crear un entorno virtual para aislar las dependencias del proyecto. Para ello, usa venv: python -m venv env


2. Activar el entorno virtual:

    En Windows:

    .\env\Scripts\activate


3. Instalar las dependencias: 
    Una vez activado el entorno virtual, instala las dependencias del proyecto listadas en el archivo requirements.txt: pip install -r requirements.txt


4. Aplicar migraciones de la base de datos: 
    Ejecuta las migraciones de la base de datos para crear las tablas necesarias: python manage.py migrate


5. Crear un superusuario (opcional, pero recomendado para acceder al admin de Django): 
    python manage.py createsuperuser


6. Ejecutar el servidor de desarrollo: 
    Finalmente, inicia el servidor de desarrollo de Django: python manage.py runserver


7. Por último acceder al proyecto: 
    Abre un navegador web y navega a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.