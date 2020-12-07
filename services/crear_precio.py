def crear_precio(html):
    inicio_precio = html.find("'precio'")
    marca_inicial_precio = html.find(':',inicio_precio)
    marca_final_precio = html.find('<',marca_inicial_precio)
    precio = html[marca_inicial_precio+2: marca_final_precio]
    return precio, marca_final_precio