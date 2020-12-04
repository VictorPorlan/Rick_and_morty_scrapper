from urllib.request import urlopen

url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")



def crear_caracteristicas(html):
        
        caracteristicas = {}
        final_caracteristicas = html.find('</ul>')
        inicio_caracteristica = html.find('caracteristica')
        
        while final_caracteristicas > inicio_caracteristica:
                inicio_caracteristica = html.find('caracteristica')
                inicio_nombre = html.find('>',inicio_caracteristica)
                final_nombre = html.find(':',inicio_caracteristica)
                nombre = html[inicio_nombre+1: final_nombre]
                final_caracteristica = html.find('<',inicio_nombre)
                caracteristica = html[final_nombre+2: final_caracteristica]
                caracteristicas[nombre] = caracteristica
                html= html[final_caracteristica:]
                final_caracteristicas = html.find('</ul>')
                inicio_caracteristica = html.find('caracteristica')
        return caracteristicas, final_caracteristica

def crear_objeto(html):
        objeto = {}
        localizador_objeto = html.find('objeto')
        inicio_nombre = html.find('objeto')
        marca_inicial_nombre = html.find('>',inicio_nombre)
        marca_final_nombre = html.find('<',inicio_nombre)
        nombre_pack = html[marca_inicial_nombre +1:marca_final_nombre]
        objeto['nombre'] = nombre_pack
        html = html[marca_final_nombre:]
        caracteristicas, final_caracteristica = crear_caracteristicas(html)
        objeto['caracteristicas'] = caracteristicas
        return objeto, final_caracteristica

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
        final_pack = html.find('</div>')
        objeto, final_caracteristica = crear_objeto(html)
        html = html[final_caracteristica:]
        pack['objetos']=[objeto]
        while final_pack > final_caracteristica:
                objeto, final_caracteristica = crear_objeto(html)
                html = html[final_caracteristica:]
                pack['objetos']=[objeto]
                print (pack)
        return pack

print (crear_paquetes(html_link))
