from urllib.request import urlopen

link_index_pagina = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"

def sacar_html(index):
    page = urlopen(index)
    html_bytes = page.read()
    html_index = html_bytes.decode("utf-8")
    assert isinstance(html_index, str)
    return html_index
#print (sacar_html("https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"))


def conseguir_links(index):
    codigo_fuente_index = sacar_html(index)
    lista_links = []
    inicio_menu = codigo_fuente_index.find('ul class="horizontal"')
    final_menu = codigo_fuente_index.find('>/ul>', inicio_menu)
    menu = codigo_fuente_index[inicio_menu: final_menu]
    for texto in menu:
        marca_izquierda = 'a href='
        marca_derecha = '<a>'
        if marca_izquierda
        inicio_link = menu.find(marca_izquierda) + len(marca_izquierda)
        final_link = menu.find(marca_derecha)
        link = menu[inicio_link : final_link]        
        lista_links.append(link)
    return lista_links
print(conseguir_links("https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"))


if __name__ == "__main__":
    pass
