from urllib.request import urlopen
from crawling import conseguir_links
def bucle_crawler():
        for link in conseguir_links:
                url = link
                page = urlopen(url)
                html_bytes = page.read()
                html_link = html_bytes.decode("utf-8")
        def crear_caracteristicas(html):
                listado = {}
                final_caracteristicas = html.find('/section')
                inicio_caracteristica = html.find('caracteristica')
                while final_caracteristicas > inicio_caracteristica:
                        inicio_nombre = html.find('>',inicio_caracteristica)
                        final_nombre = html.find(':',inicio_nombre)
                        nombre = html[inicio_nombre+1: final_nombre]
                        final_caracteristica = html.find('<',inicio_nombre)
                        caracteristica = html[final_nombre+2: final_caracteristica]
                        listado[nombre] = caracteristica
                        html= html[final_caracteristica:]
                        final_caracteristicas = html.find('/section')
                        inicio_caracteristica = html.find('caracteristica')
                html = html[final_caracteristicas+3:]
                return listado, html
        print bucle_crawler()