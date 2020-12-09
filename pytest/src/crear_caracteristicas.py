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
                if inicio_caracteristica == -1:
                        break
        html = html[final_caracteristicas+3:]
        return listado, html