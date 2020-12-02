import crawling
from urllib.request import urlopen

url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

def localizar_paquetes(html):
        pack = {}
        inicio_pack = html.find('nombre')
        inicio_nombre = html.find('>', inicio_pack)
        final_nombre = html.find('<', inicio_nombre)
        nombre = html[inicio_nombre+1:final_nombre]
        pack['name'] = nombre
        return inicio_pack

print(localizar_paquetes(html))

def convertir_link_string(enlace):
        page = urlopen(enlace)
        html_bytes = page.read()
        html_link = html_bytes.decode("utf-8")
def sinNombre(html):
        conseguir_links(html)
        for enlace in links:
                convertido = convert_link_string(enlace)


        
