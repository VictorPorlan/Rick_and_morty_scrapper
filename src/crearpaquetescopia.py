
from urllib.request import urlopen
from crear_objeto import crear_objeto
from crear_caracteristicas import crear_caracteristicas
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")

def crear_paquetes(html):
        pack = {}
        inicio_pack = html.find('nombre')
        marca_inicial_nombre = html.find('>', inicio_pack)
        marca_final_nombre = html.find('<', marca_inicial_nombre)
        nombre = html[marca_inicial_nombre+1:marca_final_nombre]

        pack['name'] = nombre

        inicio_dimensiones = html.find('altura')
        marca_inicial_altura = html.find(':',inicio_dimensiones)
        marca_final_altura = html.find('<',inicio_dimensiones)
        altura = html[marca_inicial_altura+2 : marca_final_altura]
        inicio_ancho = html.find('ancho')
        marca_inicial_ancho = html.find(':',inicio_ancho)
        marca_final_ancho = html.find('<',inicio_ancho)
        ancho = html[marca_inicial_ancho+2 : marca_final_ancho]

        pack['dimensiones'] = {'altura':altura, 'ancho':ancho}
        
        html = html[marca_final_ancho:]
        objeto, html = crear_objeto(html)
        carac, html, nombre_pack = crear_objeto(html)
        final_pack = html.find('/div')
        final_caracteristicas = html.find('section')
        pack['objetos']=[objeto]
        pack[nombre_pack]=carac
        while final_pack > final_caracteristicas:
                objeto, html = crear_objeto(html)
                pack['objetos'].append(objeto)
                carac, html, nombre_pack = crear_objeto(html)
                pack[nombre_pack] = carac
                final_caracteristicas = html.find('section')
                final_pack = html.find('/div')
                if final_caracteristicas == -1:
                    return pack
