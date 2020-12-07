from crear_caracteristicas import crear_caracteristicas

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
