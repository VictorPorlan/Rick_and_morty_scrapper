from urllib.request import urlopen
from crear_objeto import crear_objeto
from crear_caracteristicas import bucle_crawler
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")


pack = {}
#### Por el momento he estado intentando al menos dividir la función, no sé si rula porque no a mí no me deja
# hacer los prints si hay imports no resueltos.Pruébalo tú, porfa. No sé qué pasa con los import.
##### Tranquilo! Si no funciona, podemos intentarlo con un closure o si eso tampoco funciona
#si quitas los dos def que hay de más y lo que te marco con comentario, se queda como antes.
def crear_paquetes_pack(html):
        inicio_pack = html.find('nombre')
        marca_inicial_nombre = html.find('>', inicio_pack)
        marca_final_nombre = html.find('<', marca_inicial_nombre)
        nombre = html[marca_inicial_nombre+1:marca_final_nombre]

        pack['name'] = nombre
        return pack #esto habría que borrarlo si no funciona
def crear_paquetes_altura(html):
        inicio_dimensiones = html.find('altura')
        marca_inicial_altura = html.find(':',inicio_dimensiones)
        marca_final_altura = html.find('<',inicio_dimensiones)
        altura = html[marca_inicial_altura+2 : marca_final_altura]
        inicio_ancho = html.find('ancho')
        marca_inicial_ancho = html.find(':',inicio_ancho)
        marca_final_ancho = html.find('<',inicio_ancho)
        ancho = html[marca_inicial_ancho+2 : marca_final_ancho]

        pack['dimensiones'] = {'altura':altura, 'ancho':ancho}
        return pack,marca_final_ancho #esto habría que borrarlo si no funciona
def integrar_paquete(html):
        inicio_ancho = html.find('ancho') #esto también porque está en la función anterior (sería repetirse)
        marca_final_ancho = html.find('<',inicio_ancho)#esto también porque está en la función anterior (sería repetirse)
        html = html[marca_final_ancho:]
        carac, html, nombre_pack = crear_objeto(html)
        final_pack = html.find('/div')
        final_caracteristicas = html.find('section')
        pack[nombre_pack]=carac
        while final_pack > final_caracteristicas:
                carac, html, nombre_pack = crear_objeto(html)
                pack[nombre_pack] = carac
                final_caracteristicas = html.find('section')
                final_pack = html.find('/div')
                if final_caracteristicas == -1:
                        break
        return pack,html 
        print (integrar_paquete(html_link))
