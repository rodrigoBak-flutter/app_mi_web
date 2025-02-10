## Para crear un entorno virtual, utiliza: ##
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

## SI SALE ESTE ERROR: 
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

Debemos ejecutar
python manage.py migrate

Configurar el administrador 
http://localhost/admin/login/?next=/admin/

## Crear Super user
python manage.py createsuperuser
crear usuario y contraseña para tener acceso

## CREAR APP##
SIEMPRE ESTANDO CON NUESTRO ENTORNO VITUAL ACTIVO CREAMOS 
python manage.py startapp base 

## DEFINIR LOS MODELOS Y DESPUES CREAR LAS TABLAS EN LA BBDD##
python manage.py makemigrations y python manage.py sqlmigrate base 0001(este 0001 te lo da cuando haces la migracion, puede ser 0002,5,10, etc)

A modo de ejemplo, te devuelve las tablas creadas Migrations for 'base':
  base\migrations\0001_initial.py
    + Create model Articles
    + Create model Client
    + Create model Orders

y por ultimo cuando ya este todo incluido:
python manage.py migrate 

Operations to perform:                                                                                                                           
  Apply all migrations: admin, auth, base, contenttypes, sessions
Running migrations:
  Applying base.0001_initial... OK

## PRUEBA DE SI TODO VA BIEN EN LA APLICACAION##
python manage.py check base



## CREACION DE BBDD POSTGRESQL##
Dentro de Query tools puedo agregar mis comandos para creacion consulta, y demas.

create database ArticlesClients 

respuesta
CREATE DATABASE
Query returned successfully in 563 msec.

Hacer un refresh

## Conexion con nuestra BBDD POSTGRESQL##
pip install psycopg2

configurar los setting.py 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ELNOMBREDETUBBDD',
        'USER': 'postgres',
        'PASSWORD': 'TUCLAVE', 
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Soltar  
python manage.py makemigrations
python manage.py migrate

Insertar desde la consola un usaurio(por ejemplo)
python manage.py shell 

## Creo mi modelo
from base.models import Client

## Creo una variable
client=Client(name='Rodrigo',address='Asturias 23',email='test@test.com',phone='654236178')
client.save()

## Consultas por secciones(where) en mi 
from base.models import Articles
Articles.objects.filter(section='Deporte')

## agregar en nuestro modelo
#Con esto me devuelve raqueta, la seccion, el nombre, precio
    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' %(self.name, self.section,self.price)
python manage.py makemigrations
python manage.py migrate
auque no haga nada, si que hace despues repetir el proceso:
respuesta = <QuerySet [<Articles: El nombre es Paleta la seccion es Deporte y el precio es 150.80>]>


## Consulta mas restrictiva
Articles.objects.filter(name'Mesa',section='Hogar') 

Ordenar ascendente, de menor a mayor
Articles.objects.filter(price__gte =50).order_by('price')

Ordenar descendente, de mayor a menor
Articles.objects.filter(price__gte =50).order_by('-price')


## CAMBIO DE IDIOMA DE MI PANEL DE CONTROL ADMIN###
SETTINGS:PY ===> LANGUAGE_CODE = 'en-us'EEUU(por defecto)   LANGUAGE_CODE = 'es-es'ESPAÑOL     LANGUAGE_CODE = 'es-ar' ARGENTINA 


## ENVIAR CORREOS DESDE LA CONSOLA POWERSHELL(Antes debemos configurar nuesto setting.py)

EMAIL="django.core.email.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="TUCORREO"
EMAIL_HOST_PASSWORD="TUPASSWORD"


from django.core.mail import send_mail
send_mail('Asunto','Mensaje', 'CORREO_QUE_EMVIA', ['CORREO_QUE_RECIBE'],fail_silently=False)
