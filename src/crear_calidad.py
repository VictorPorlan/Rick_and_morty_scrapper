def crear_calidad(html):
    inicio_calidad = html.find("calidad")
    marca_inicial_calidad= html.find('>',inicio_calidad)
    marca_final_calidad= html.find('<',marca_inicial_calidad)
    calidad = html[marca_inicial_calidad+1:marca_final_calidad]
    return calidad, marca_final_calidad