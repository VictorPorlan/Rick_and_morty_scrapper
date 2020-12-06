from urllib.request import urlopen
from crawling import conseguir_links

def borrar_link_index(index):
    links_sin_index = conseguir_links(index)
    links_sin_index.remove(index)
    return links_sin_index
print (borrar_link_index("https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"))

def todas_paginas_codigo_fuente():
    paginas_string = ''
    for link in conseguir_links:  
        page = urlopen(link)
        html_bytes = page.read()
        html_index = html_bytes.decode("utf-8")
        paginas_string += html_index
#no me resuelve el import