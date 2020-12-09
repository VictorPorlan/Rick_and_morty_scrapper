from src.crear_caracteristicas import crear_caracteristicas

def crear_objeto(html):
        carac = {}
        inicio_nombre = html.find('objeto')
        marca_inicial_nombre = html.find('3>',inicio_nombre)
        marca_final_nombre = html.find('<',marca_inicial_nombre)
        nombre_pack = html[marca_inicial_nombre+2:marca_final_nombre]
        html = html[marca_final_nombre:]
        caracteristicas, html = crear_caracteristicas(html)
        carac['caracteristicas'] = caracteristicas
        return carac, html, nombre_pack
