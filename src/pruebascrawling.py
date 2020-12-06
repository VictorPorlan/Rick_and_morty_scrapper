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
    html_index = sacar_html(index)
    lista_links = []
    while html_index.find('a href') != -1:
        inicio = html_index.find("a href='") + len("a href='")
        final = html_index.find(">", inicio)
        link = html_index[inicio:final]
        lista_links.append(link)
        html_index = html_index[final:]
    return lista_links
if __name__ == "__main__":
    assert conseguir_links(link_index_pagina) == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html']
