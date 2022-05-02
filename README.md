# proyectoDemoCostos
### Proyecto demo para el área de costos

#### Para poder ejectuar este proyecto se debe de tener instalado python y Dango, ademas es requerido instalar ciertas librerias y paquetes que son necesarios para el correcto funcionamiento del proyecto. A continuación se listan los comandos para instalar dichas librerias y paquetes:

* pip install Django = 3.2.13
* pip install mssql-django==1.0rc1
* pip install pillow
* pip install django-crispy-forms
* pip install django-betterforms
* pip install six


##### Como nota importante, en el archivo settings donde se configura la base de datos, se deben de poner los datos correspondientes a sus credenciales y el nombre del servidor local que tengan en su PC.



    'default': {
        'ENGINE': 'mssql',
        'NAME':'C_CDATABASE',
        'USER': 'NOMBRE_USUARIO_INICIO_SESION_SQL_SERVER',
        'PASSWORD': 'CONTRASEÑA_INICIO_SESION_SQL_SERVER',
        'HOST': 'NOBRE_SERVIDOR_LOCAL',  
        'PORT': '',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
