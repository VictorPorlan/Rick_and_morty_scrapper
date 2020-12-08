from src.crear_objeto import crear_objeto
def crear_contenidos(html):
    final_pack = html.find('/div')
    final_caracteristicas = html.find('/section')
    contenidos = {}
    while final_pack > final_caracteristicas:
        carac, html, nombre_pack = crear_objeto(html)
        contenidos[nombre_pack] = carac
        final_caracteristicas = html.find('/section')
        final_pack = html.find('/div')
        if final_caracteristicas == -1:
            break
    return contenidos, html
        
