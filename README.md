##Para crear un entorno virtual, utiliza: ##
python -m virtualenv web   (web en este caso).


Después de crear el entorno, actívalo según tu sistema operativo:
web\Scripts\activate  (web en este caso)


creamos la carpeta src(mi fuente)
mkdir src
cd src para navegar

django-admin startproject mi_web

correr la app
cd mi_web (llamda asi en este caso)

python manage.py runserver 

SI SALE ESTE ERROR: 
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

Debemos ejecutar
python manage.py migrate

Configurar el administrador 
http://localhost/admin/login/?next=/admin/

Crear Super user
python manage.py createsuperuser
crear usuario y contraseña para tener acceso

##CREAR APP##
SIEMPRE ESTANDO CON NUESTRO ENTORNO VITUAL ACTIVO CREAMOS 
python manage.py startapp base 