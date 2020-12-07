def crear_dimensiones(html):
    inicio_dimensiones = html.find('altura')
    marca_inicial_altura = html.find(':',inicio_dimensiones)
    marca_final_altura = html.find('<',inicio_dimensiones)
    altura = html[marca_inicial_altura+2 : marca_final_altura]
    inicio_ancho = html.find('ancho')
    marca_inicial_ancho = html.find(':',inicio_ancho)
    marca_final_ancho = html.find('<',inicio_ancho)
    ancho = html[marca_inicial_ancho+2 : marca_final_ancho]
    return altura, ancho, marca_final_ancho