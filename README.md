# Proyecto Packs Amenities
![Alt Text](https://media1.tenor.com/images/41d4482a7391e4ced853f5cdb83be9cd/tenor.gif?itemid=4750015)
## Explicación
Para el presente proyecto hemos creado un sitio web (usando html y css) de venta de paquetes de bienvenida para una fiesta con temática de Rick y Morty. Una vez hecha la página y añadida toda la información, hemos desarrollado un programa en Python 3  capaz de, a partir de una página raíz, extraer todos los enlaces del sitio web (obviando los que están repetidos) mediante un crawler, y scrappear toda la información de los paquetes de bienvenida (esto es, cuál es su precio, qué objetos contienen, etc.) para meterla en un diccionario y la subirla a una base de datos MongoDB en formato Json. Para conseguir todo esto hemos usado librerías como urllib, request o pymongo.

## Utilización

**Para hacer uso de la aplicación es necesario instalar todas las libreríaas listadas en el archivo requirements.txt.:**
- Para ello es conveniente que instales venv (para entornos virtuales) antes de clonar el proyecto.
`$ sudo apt-get install python3.6-venv`
- Después crea un directorio y sitúate en él.
```bash
$ mkdir ./fiestaRick
$ cd fiestaRick
```
- Una vez creado el directorio donde quieres almacenar el proyecto, clona el repositiorio.
    `$ git clone https://github.com/BertaVR/Proyecto_Rick_y_Morty.git`
- Después de haber clonado el proyecto, es el momento de crear el entorno virtyal e inicializarlo.
    `$ python3.6 -m venv venv`
    `$ source venv/bin/activate`
- Como último paso antes de poder lanzar el proyecto, hay que instalar las dependencias del fichero requirements.txt 
    `$ pip install -r requirements.txt`
- Para lanzar el archivo python lo puedes lanzar desde consola indicando la ruta ( recuerda que la ruta será la ruta donde has creado el directorio seguida de `/fiestaRick/Proyecto_Rick_Y_Morty/services/app.py`)
    `$ python3 <ruta del fichero>/app.py`

Alternativamente, puedes ejecutar el fichero app.py (el cual se encuentra dentro del directorio services) desde un IDE. 

Para visualizar nuestro sitio web, este es el enlace: [página principal venta de amenities](https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html).

Si en vez de entrar en la web a través de el enlace pretendes visualizar las páginas web desde los archivos html que hay en el repositorio, recuerda instalar las tipografías. 
## Autores
Autores: Berta Verges y Víctor Porlan
Gracias a todos los profesores de DAW dual por toda la ayuda y a nuestro mentor Mateu Massó por dedicar parte de su tiempo a ayudarnos con todas nuestras dudas.


