from urllib.request import urlopen
import re

link_index_pagina = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"

def sacar_html(link_index): 
#esto es lo que saca html, lo he puesto en función para poder usarlo en el crawler y en el bucle sin estar copiando cada vez
    page = urlopen(link_index)
    html_bytes = page.read()
    html_index = html_bytes.decode("utf-8")
    assert isinstance(html_index, str)
    return html_index


def conseguir_links(link_index):
    #esto es el crawler
    lista_links = [link_index]
    for pagina in lista_links:
        html_pagina = sacar_html(pagina)
        linksRegex = re.compile(r'a href=(\'|\")(.*?)\.\S(\'|\")>')
        mo_links = linksRegex.findall(html_pagina)
    for link in mo_links:
        if link in lista_links or mo_links.count(link) > 1:
            mo_links.remove(link)
    lista_links = lista_links + mo_links
    assert isinstance(lista_links, list)
    return lista_links

if __name__ == "__main__": 
    assert conseguir_links(link_index_pagina) == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html']