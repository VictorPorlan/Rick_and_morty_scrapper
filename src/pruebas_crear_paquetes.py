from urllib.request import urlopen
from pruebascrawling import crawl_conseguir_html, lista_codigos_fuente, link_index_pagina
from crear_objeto import crear_objeto
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")
pack = {}
def nombre_packs(html):  
        while html.find('class="nombre">') != -1:
                inicio_nombre_pack = html.find('class="nombre">') + len('class="nombre">')
                final_nombre_pack = html.find('<', inicio_nombre_pack)
                nombre = html[inicio_nombre_pack:final_nombre_pack]
                pack['Nombre pack'] = nombre
                html = html[final_nombre_pack : ]
        return pack




def calidad_packs(html):
        html.split('/div')
        for pack in html:
                inicio_calidad = html.find("'calidad>'") + len("'calidad'")
                final_calidad= html.find('<', inicio_calidad)
                calidad = html[inicio_calidad : final_calidad]
                pack['calidad'] = calidad
        return pack 
        print(calidad_packs(crawl_conseguir_html(link_index_pagina)))
def dimensiones_packs(html):
        html.lower()
        while html.find('ancho:') != -1:
                inicio_altura= html.find('altura:') + len('altura:')
                final_altura = html.find('<',inicio_altura)
                altura = html[inicio_altura :final_altura]
                inicio_ancho = html.find('ancho:') + len('ancho:')
                final_ancho = html.find('<',inicio_ancho)
                ancho = html[inicio_ancho : final_ancho]
                pack['dimensiones'] = {'altura':altura, 'ancho':ancho}
                html = html[final_ancho : ]
        return pack
def pack_y_objetos_integrar():
                carac, html, nombre_pack = crear_objeto(html)
                final_pack = html.find('/div')
                final_caracteristicas = html.find('section')
                pack[nombre_pack]=carac
                while final_pack > final_caracteristicas:
                        carac, html, nombre_pack = crear_objeto(html)
                        pack[nombre_pack] = carac
                        final_caracteristicas = html.find('section')
                        final_pack = html.find('')
                        if final_caracteristicas == -1:
                                break
                
        return pack,html
