import crawling
from urllib.request import urlopen

url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

def crear_paquetes(html):
        pack = {}
        inicio_pack = html.find('nombre')
        marca_inicial_nombre = html.find('>', inicio_pack)
        marca_final_nombre = html.find('<', marca_inicial_nombre)
        nombre = html[marca_inicial_nombre+1:marca_final_nombre]

        pack['name'] = nombre

        inicio_dimensiones = html.find('altura')
        marca_inicial_altura = html.find('>',inicio_dimensiones)
        marca_final_altura = html.find('<',inicio_dimensiones)
        altura = html[marca_inicial_altura+1 : marca_final_altura]

        inicio_ancho = html.find('ancho')
        marca_inicial_ancho = html.find('>',inicio_ancho)
        marca_final_ancho = html.find('<',inicio_ancho)
        
        ancho = html[marca_inicial_ancho+1 : marca_final_ancho]

        pack['dimensiones'] = {altura, ancho}
        


        return pack

print(crear_paquetes(html))

def convertir_link_string(enlace):
        page = urlopen(enlace)
        html_bytes = page.read()
        html_link = html_bytes.decode("utf-8")
def sinNombre(html):
        conseguir_links(html)
        for enlace in links:
                convertido = convert_link_string(enlace)


        
