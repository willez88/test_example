# Ejempĺo de Prueba

# Pasos para crear el entorno de desarrollo

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

Probado en Debian 9 y Ubuntu 18.04. Instalar los siguientes programas

    ~# apt install curl git graphviz graphviz-dev postgresql phppgadmin python3-dev virtualenv

Para instalar npm hacer lo siguiente

    ~# curl -sL https://deb.nodesource.com/setup_10.x | bash -

    ~# apt install -y nodejs

Crear las siguientes carpetas

    ~$ mkdir Programación

Desde el terminal, moverse a la carpeta Programación y ejecutar

    ~$ cd Programación/

    ~$ mkdir python

Entrar a la carpeta python y hacer lo siguiente

    ~$ cd python/

    ~$ mkdir entornos_virtuales proyectos_django

Entrar a entornos_virtuales

    ~$ cd entornos_virtuales/

    ~$ mkdir django

Desde el terminal, moverse a la carpeta django y ejecutar

    ~$ cd django/

    ~$ virtualenv -p python3 test_example

Para activar el entorno

    ~$ source test_example/bin/activate

Nos movemos a la carpeta proyectos_django, descargamos el sistema y entramos a la carpeta con los siguientes comandos

    (test_example) ~$ cd ../../proyectos_django/

    (test_example) ~$ git clone https://github.com/willez88/test_example.git

    (test_example) ~$ cd test_example/

    (test_example) ~$ cp test_example/settings.py_example test_example/settings.py

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/python/entornos_virtuales/django/test_example

    // Servidor de desarrollo
    Programación/python/proyectos_django/test_example

Instalar las dependencias de css y js: moverse a la carpeta static y ejecutar

    (django_example) ~$ cd static/

    // Usa el archivo package.json para instalar lo que ya se configuro allí
    (test_example) ~$ npm install

    // Terminado el proceso volver a la carpeta raíz del proyecto
    (test_example) ~$ cd ../

Crear la base de datos para __test_example__ usando PostgresSQL

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de PostgreSQL
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH LOGIN ENCRYPTED PASSWORD '123' CREATEDB;
    postgres=# \q

    // Desautenticar el usuario PostgreSQL y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos usando la interfaz gráfica phppgadmin

    // Desde algún navegador ir al siguiente sitio y entrar con el usuario que se acaba de crear
    localhost/phppgadmin

    // Nombre de la base de datos: test_example

Instalamos los requemientos que el sistema necesita en el entorno virtual

    (test_example) ~$ pip install -r requirements/dev.txt

Hacer las migraciones

    (test_example) ~$ python manage.py makemigrations base user

    (test_example) ~$ python manage.py migrate

    (test_example) ~$ python manage.py loaddata 1_country.json 2_state.json 3_city.json academic_level.json

Crear usuario administrador

    (test_example) ~$ python manage.py createsuperuser

Correr el servidor de django

    (test_example) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para entrar el sistema

Llegado hasta aquí el sistema ya debe estar funcionando

Para salir del entorno virtual se puede ejecutar desde cualquier lugar del terminal: deactivate

Grafica el modelo de datos usando el paquete pygraphviz

    (test_example) ~$ python manage.py graph_models -a -g -o test_example.svg