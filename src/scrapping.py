from src.crawling import localizar_links, conseguir_links, links
from urllib.request import urlopen

def localizar_paquetes(html):
        pack = {}
        inicio_pack = html.find('<div class="pack">')+17
        inicio_nombre = html.find('>', inicio_pack)
        final_nombre = html.find('<', inicio_nombre)
        nombre = html[inicio_nombre+1:final_nombre]
        pack['name'] = nombre
        return pack

def convertir_link_string(enlace):
        page = urlopen(enlace)
        html_bytes = page.read()
        html_link = html_bytes.decode("utf-8")
def sinNombre(html):
        conseguir_links(html)
        for enlace in links:
                convertido = convert_link_string(enlace)


        
