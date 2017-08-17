# Web Sites Monitor

En el proyecto se incluye el archivo requirements.txt que contiene las librerias necesarias para correrlo, para instalar las librerias
se necesita ejecutar en la terminal el comando (ubicados en el directorio raíz del proyecto):
 pip install -r requirements/local.txt

Al finalizar la instalación ejecutar:
    python manage.py migrate

Hay un fixture cargado para cargar información inicial, el usuario es admin y la contraseña es adminqwerty.

Para cargarlo ejecutar el comando:
 python manage.py loaddata fixtures/01-initial.json

Para ejecturalo se debe ejecutar el comando:
    python manage.py runserver

La configuración del tiempo y de la url a verificar se puede realizar desde el admin de Django en el módulo Configurations, por ejemplo:
 http://localhost:8000/admin/Monitor/configuration/

Realizada la configuración ṕuede visualizar el monitor en la pagina principal:
    http://localhost:8000/

Para visualizar la tabla de las verificaciones realizadas es en la siguiente URL:
    http://localhost:8000/administration/

Se genera un archivo CSV en la raíz del proyecto con el nombre file-monitoring.csv con los registros de las verificaciones realizadas.

Se genera un archivo nombrado debug.log con información de las peticiones realizadas en el proyecto.

