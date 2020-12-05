from urllib.request import urlopen
from src.crear_caracteristicas import crear_caracteristicas
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")

def crear_objeto(html):
        objeto = {}
        inicio_nombre = html.find('objeto')
        marca_inicial_nombre = html.find('3>',inicio_nombre)
        marca_final_nombre = html.find('<',marca_inicial_nombre)
        nombre_pack = html[marca_inicial_nombre+2:marca_final_nombre]
        objeto['nombre'] = nombre_pack
        html = html[marca_final_nombre:]
        caracteristicas, html = crear_caracteristicas(html)
        objeto['caracteristicas'] = caracteristicas
        return objeto, html
