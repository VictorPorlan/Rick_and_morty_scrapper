from urllib.request import urlopen
from crear_caracteristicas import crear_caracteristicas
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")

def crear_objeto(html):
        dicc_caract = {}
        inicio_nombre = html.find('objeto')
        inicio_nombre = html.find('h3>',inicio_nombre) + len('h3>')
        marca_final_nombre = html.find('<',inicio_nombre)
        nombre_pack = html[inicio_nombre : marca_final_nombre]
        html = html[marca_final_nombre: ]
        caracteristicas, html = crear_caracteristicas(html)
        dicc_caract['caracteristicas'] = caracteristicas
        return dicc_carac, html, nombre_pack
