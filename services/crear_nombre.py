def crear_nombre(html):
    inicio_pack = html.find('nombre')
    marca_inicial_nombre = html.find('>', inicio_pack)
    marca_final_nombre = html.find('<', marca_inicial_nombre)
    nombre = html[marca_inicial_nombre+1:marca_final_nombre]
    return nombre, marca_final_nombre