# Challenge_Alkemy

##Para el proyecto debe descargarse python y pip, se debe descargar desde: https://www.python.org

###Librerias y componentes necesarios para el proyecto (todos se pueden instalar con pip):

* requests

* pandas

* virtualenv

* sqlalchemy

* python-decouple

* logging 

* pymssql

###Consideraciones para el correcto funcionamiento del proyecto:
Se debe especificar la ruta donde va a estar el proyecto y cambiar la misma en las partes del codigo donde se pida


###Entorno virtual:

#Como crear el entorno virtual donde se va a ejecutar el proyecto:

* En una consola vamos a ir con el comando "cd" hasta llegar al directorio donde queramos alojar el entorno virtual

* Ya en el directorio, corremos el comando "virtualenv" seguido del nombre que queramos ponerle

* Seguido de esto activamos el entorno virtual haciendo .\"nombre del entorno"\Scripts\activate (Para saber si ya estamos en el entorno, a la izquierda deberia aparecernos el nombre)

* Instalamos todas las librerias que vamos a usar en el entorno virtual con pip
(colocando el comando pip freeze podemos ver si ya se instalaron)

* Para correr un programa escribimos python "nombre del archivo.py"


###Base de datos:

Creamos la base de datos "db_alkemy" en pgadmin 4

Para conectarnos a la base de datos usamos esta linea de codigo

create_engine("postgresql://postgres:admin@localhost:5432/db_alkemy")

admin es la contraseña de la base de datos 

El puerto es 5432 

El nombre de la base de datos es db_alkemy
